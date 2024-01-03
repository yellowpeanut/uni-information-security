class ElGammalCoder:

    def __init__(self):
        pass

    def encrypt(self, alphabet, message, keyword):
        hashTable = self.__createHashTable(alphabet)
        mess = list(message)
        kw = list(keyword)
        kwlen = len(kw)
        res = ""
        for i, symb in enumerate(mess):
            num = hashTable[symb] + hashTable[kw[i%kwlen]]
            res += f"{num:03d}"
        return res

    def decrypt(self, pub_key, priv_key, message, chunkSize):
        p, g = pub_key[0], pub_key[1]
        x = priv_key
        y = (g**x)%p
        res = ""
        bts = []
        # need to know how to split that thing :/
        chunks = [message[i:i+chunkSize*3] for i in range(0, len(message), chunkSize*3)]
        print(chunks)

        for chunk in chunks:
            symbols = [chunk[i:i+3] for i in range(0, len(chunk), 3)]
            print(symbols)
            a = int(symbols.pop(0))
            for s in symbols:
                print(a, s, int(s))
                # m = (int(s)/(a**x))%p
                m = (int(s)*(a**(p-1-x)))%p
                print(m)
                bts.append(m)

        print(bts)
        res = bytes(bts).decode("utf-8")
        print(res)
        return res

    def __createHashTable(self, alphabet):
        hashTable = {}
        ab = list(alphabet)
        for i, symb in enumerate(ab):
            hashTable[symb] = i
        return hashTable
    