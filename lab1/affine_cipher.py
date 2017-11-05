import math
from base_cipher import *


def phi(x):
    num_coprimes = 0
    for i in range(1, x):
        if math.gcd(i, x) == 1:
            num_coprimes +=1
    return num_coprimes


class AffineCipher(BaseCipher):
    def __init__(self, plaintext, ciphertext, key, alphabet):
        encrypter = AffineEncrypter(plaintext, ciphertext, key)
        decrypter = AffineDecrypter(plaintext, ciphertext, key)
        mapper = Mapper(alphabet, range(len(alphabet)))
        super().__init__(encrypter, decrypter, mapper)


class AffineEncrypter(BaseEncrypter):
    def __init__(self, plaintext, ciphertext, key):
        """
        plaintext must equal ciphertext
        key is a pair (a,b)
        gcd(a, n) must be 1, where n is len(plaintext)
        """
        super().__init__(plaintext, ciphertext, key)
        self.n = len(plaintext)
        self.a, self.b = key

    def encrypt(self, text):
        encrypted_text = []
        for character in text:
            encrypted_character = (self.a * character + self.b) % self.n
            encrypted_text.append(encrypted_character)
        return encrypted_text


class AffineDecrypter(BaseDecrypter):
    def __init__(self, plaintext, ciphertext, key):
        """
        plaintext must equal ciphertext
        key is a pair (a,b)
        gcd(a, n) must be 1, where n is len(plaintext)
        """
        super().__init__(plaintext, ciphertext, key)
        self.n = len(plaintext)
        self.a, self.b = key
        self.a_inv = (self.a ** (phi(self.n)-1)) % self.n

    def decrypt(self, text):
        decrypted_text = []
        for character in text:
            decrypted_character = self.a_inv * (character - self.b + self.n) % self.n
            decrypted_text.append(decrypted_character)
        return decrypted_text
