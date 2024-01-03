class GOSTCoder:

    def __init__(self):
        import os
        self.KEYPATH = os.path.dirname(__file__) + "/key.txt"
        self.two32 = 2**32
        self.NUM_ROUNDS = 32
        self.chunkSize = 64
        self.hashTable = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 1,
            10: 2,
            11: 3,
            12: 4,
            13: 5,
            14: 6,
            15: 7,
            16: 8,
            17: 1,
            18: 2,
            19: 3,
            20: 4,
            21: 5,
            22: 6,
            23: 7,
            24: 8,
            25: 8,
            26: 7,
            27: 6,
            28: 5,
            29: 4,
            30: 3,
            31: 2,
            32: 1
        }
        self.S = [
            {0:4, 1:10, 2:9, 3:2, 4:13, 5:8, 6:0, 7:14, 8:6, 9:11, 10:1, 11:12, 12:7, 13:15, 14:5, 15:3},
            {0:14, 1:11, 2:4, 3:12, 4:6, 5:13, 6:15, 7:10, 8:2, 9:3, 10:8, 11:1, 12:0, 13:7, 14:5, 15:9},
            {0:5, 1:8, 2:1, 3:13, 4:10, 5:3, 6:4, 7:2, 8:14, 9:15, 10:12, 11:7, 12:6, 13:0, 14:9, 15:11},
            {0:7, 1:13, 2:10, 3:1, 4:0, 5:8, 6:9, 7:15, 8:14, 9:4, 10:6, 11:12, 12:11, 13:2, 14:5, 15:3},
            {0:6, 1:12, 2:7, 3:1, 4:5, 5:15, 6:13, 7:8, 8:4, 9:10, 10:9, 11:14, 12:0, 13:3, 14:11, 15:2},
            {0:4, 1:11, 2:10, 3:0, 4:7, 5:2, 6:1, 7:13, 8:3, 9:6, 10:8, 11:5, 12:9, 13:12, 14:15, 15:14},
            {0:13, 1:11, 2:4, 3:1, 4:3, 5:15, 6:5, 7:9, 8:0, 9:10, 10:14, 11:7, 12:6, 13:8, 14:2, 15:12},
            {0:1, 1:15, 2:13, 3:0, 4:5, 5:7, 6:10, 7:4, 8:9, 9:2, 10:3, 11:14, 12:6, 13:11, 14:8, 15:12}
        ]
        import codecs
        with codecs.open(self.KEYPATH, 'r', "utf-8") as file:
                self.key = (file.read()).strip()
                file.close()
        
        if len(self.key) != 256:
            import random
            self.key = []
            for i in range(256):
                self.key.append(random.randint(0, 1))
            self.key = ''.join(str(x) for x in self.key)

            with codecs.open(self.KEYPATH, 'w', "utf-8") as file:
                file.write(self.key)
                file.close()
        
        self.k = self.__divide_chunks(self.key, 32)
        self.K = self.k * 3 + list(reversed(self.k))

    def encrypt(self, message):
        bits = ''.join(format(i, '08b') for i in bytearray(message, encoding ='utf-8'))
        bits = self.__format_to_n(bits, 64)
        res = self.__crypt_algorithm(bits, False)

        return res

    def decrypt(self, message):
        bits = self.__crypt_algorithm(message, True)
        chunks = self.__divide_chunks(bits, 8)
        for i in range(len(chunks)):
            chunks[i] = int(chunks[i], 2)
        res = bytes(chunks).decode("utf-8")
        return res

    def __crypt_algorithm(self, bits, reversed):
        res = ""
        chunks = self.__divide_chunks(bits)

        for chunk in chunks:
            H = chunk[:len(chunk)//2]
            L = chunk[len(chunk)//2:]

            for i in range(self.NUM_ROUNDS):
                if not reversed:
                    X = self.__format_to_n(
                        bin((int(L, 2) + int(self.K[i], 2)) % self.two32)[2:], 
                        32)
                else:
                    X = self.__format_to_n(
                        bin((int(L, 2) + int(self.K[-(i+1)], 2)) % self.two32)[2:], 
                        32)
                x = self.__divide_chunks(X, 4)
                y = []
                for j in range(len(x)):
                    # encrypting with S blocks
                    y.append(self.__format_to_n(
                        (bin(self.S[j][int(x[j], 2)])[2:]),
                        4))
                Y = "".join(y)
                # bitwise circular shift to the left
                Z = Y[11:] + Y[:11]
                # modulo 2 addition
                H = self.__format_to_n((bin(int(H, 2) ^ int(Z, 2))[2:]), 32)

                if i != self.NUM_ROUNDS-1:
                    tmp = H
                    H = L
                    L = tmp
            C = H+L
            res += C

        return res
    
    def __format_to_n(self, bits, n):
        modN = len(bits)%n
        if modN != 0:
            bits = ("0"*(n - modN)) + bits
        return bits

    def __divide_chunks(self, l, n=64):
        res = []
        for i in range(0, len(l), n): 
            x = i 
            res.append(l[x:x+n])
        return res