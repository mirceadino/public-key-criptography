import math
from base_cipher import *


def phi(x):
    num_coprimes = 0
    for i in range(1, x):
        if math.gcd(i, x) == 1:
            num_coprimes +=1
    return num_coprimes


def invmod(x, n):
    return x**(phi(n)-1) % n


def det(x):
    return x[1][1] * x[0][0] - x[1][0] * x[0][1]


class HillCipher(BaseCipher):
    def __init__(self, plaintext, ciphertext, key, alphabet):
        encrypter = HillEncrypter(plaintext, ciphertext, key)
        decrypter = HillDecrypter(plaintext, ciphertext, key)
        mapper = Mapper(alphabet, range(len(alphabet)))
        super().__init__(encrypter, decrypter, mapper)


class HillEncrypter(BaseEncrypter):
    def __init__(self, plaintext, ciphertext, key):
        """
        plaintext must equal ciphertext
        key is a 2x2 matrix represented as list: [[a,b], [c,d]]
        gcd(det(key), n) must be 1, where n is len(plaintext)
        """
        super().__init__(plaintext, ciphertext, key)
        self.n = len(plaintext)
        self.key = key

    def encrypt(self, text):
        encrypted_text = []
        if len(text) % 2 != 0:
            text.append(self.space)
        key = self.key
        for i in range(0, len(text), 2):
            vector = [text[i], text[i+1]]
            result = [vector[0] * key[0][0] + vector[1] * key[1][0], \
                      vector[0] * key[0][1] + vector[1] * key[1][1]]
            encrypted_text.append(result[0] % self.n)
            encrypted_text.append(result[1] % self.n)
        return encrypted_text


class HillDecrypter(BaseDecrypter):
    def __init__(self, plaintext, ciphertext, key):
        """
        plaintext must equal ciphertext
        key is a 2x2 matrix represented as list: [[a,b], [c,d]]
        gcd(det(key), n) must be 1, where n is len(plaintext)
        """
        super().__init__(plaintext, ciphertext, key)
        self.n = len(plaintext)
        self.key = key
        k = invmod(det(key), self.n)
        invkey = [[ key[1][1] * k, -key[0][1] * k], \
                  [-key[1][0] * k,  key[0][0] * k]]
        self.invkey = invkey
        print(self.invkey)

    def decrypt(self, text):
        decrypted_text = []
        invkey = self.invkey
        for i in range(0, len(text), 2):
            vector = [text[i], text[i+1]]
            result = [vector[0] * invkey[0][0] + vector[1] * invkey[1][0], \
                      vector[0] * invkey[0][1] + vector[1] * invkey[1][1]]
            decrypted_text.append(result[0] % self.n)
            decrypted_text.append(result[1] % self.n)
        return decrypted_text


if __name__ == "__main__":
    he = HillCipher(range(27), range(27), [[3,2],[2,5]], "_abcdefghijklmnopqrstuvwxyz")
    print(he.encrypt("help"))
    print(he.decrypt("gnnw"))
