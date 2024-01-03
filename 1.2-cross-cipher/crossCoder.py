class Cross:

    def __init__(self, top, right, bottom, left):
        self.top, self.right, self.bottom, self.left = top, right, bottom, left

    def asString(self):
        return self.top + self.right + self.bottom + self.left
    

class CrossCoder:

    def __init__(self):
        pass

    def encrypt():
        pass

    def decrypt(self, message, chunkSize, noneSymb):

        crosses = []
        for i in range(int(len(message)/4)+1):
            crosses.append(Cross("", "", "", ""))

        # fill crosses

        # if chunkSize == 3
        # ту_аесрс_зу_пааиенлтяць_енгироо.имля
        # 0 2 2 6
        # 0 1 1 3
        # 0 0 0 0

        mess = list(message)
        for i, cross in enumerate(crosses):
            ind = chunkSize - (i%chunkSize + 1)

            if len(mess) > 0:
                cross.top = self.__get(mess.pop(0), noneSymb)
            else:
                crosses.remove(cross)
                continue

            if ind <= len(mess):
                cross.left = self.__get(mess.pop(ind), noneSymb)
            else:
                continue

            if ind <= len(mess):
                cross.right = self.__get(mess.pop(ind), noneSymb)
            else:
                continue

            # either ind*3 or ind*chunkSize - needs testing
            if ind*3 <= len(mess):
                cross.bottom = self.__get(mess.pop(ind*3), noneSymb)

        res = ""
        for cross in crosses:
            res +=  cross.asString()

        return res
    
    def __get(self, symbol, noneSymbol):
        if symbol == noneSymbol:
            return ""
        return symbol