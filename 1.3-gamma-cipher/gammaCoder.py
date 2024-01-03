class GammaCoder:

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

    def decrypt():
        pass

    def __createHashTable(self, alphabet):
        hashTable = {}
        ab = list(alphabet)
        for i, symb in enumerate(ab):
            hashTable[symb] = i
        return hashTable