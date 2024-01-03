import datetime
import requests
import random
import tkinter as tk

from io import BytesIO
from tkinter import messagebox, NW
from PIL import Image, ImageTk


art_links = []
images = []


def get_random_artwork():
    url = random.choice(art_links)
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        raise Exception("Failed to retrieve an artwork")


def get_expiry_date_and_art():
    response = requests.get("https://tsii.s-ul.eu/uni/r7in3lEu")
    if response.status_code == 200:
        all_text = response.text.strip().split("\n")
        expiry_date_str = all_text.pop(0).strip()
        expiry_date = datetime.datetime.strptime(expiry_date_str, "%Y-%m-%d").date()

        if(len(art_links) == 0):
            all_text.pop(0)
            art_links.extend(all_text)

        return expiry_date
    else:
        raise Exception("Failed to retrieve expiry date and art links")


def display_art(window):
    try:
        expiry_date = get_expiry_date_and_art()
        current_date = datetime.date.today()
        if current_date < expiry_date:    
            image = Image.open(get_random_artwork())
            image_width, image_height = image.size

            _width, _height = 1280, 720
            popout_win = tk.Toplevel(window)
            popout_win.title("Artwork by Sheya Chen")
            canvas = tk.Canvas(popout_win, width=_width, height=_height)

            if image_width > _width or image_height > _height:
                # Calculate the aspect ratio for resizing
                aspect_ratio = min(_width / image_width, _height / image_height)
                new_width = int(image_width * aspect_ratio)
                new_height = int(image_height * aspect_ratio)
                image = image.resize((new_width, new_height))
                popout_win.geometry("{}x{}".format(new_width, new_height))
                canvas.config(width=new_width, height=new_height)

            images.append(ImageTk.PhotoImage(image))
            canvas.pack()
            canvas.create_image(0, 0, anchor=NW, image=images[-1])
        else:
            messagebox.showinfo("Program Expired",
                                "This program has expired. Thank you for using it!")
    except Exception as e:
        messagebox.showerror("Error", "An error occurred while retrieving the expiry date and art:\n" + str(e))


def create_gui():
    window = tk.Tk()
    window.title("Artwork Display Program")
    window.geometry("250x125")

    button = tk.Button(window, text="Display random artwork", command=lambda: display_art(window))
    button.pack(pady=50)

    window.mainloop()


create_gui()
