import random

BASE = 28


def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a


def encode(plaintext):
    message = 0
    for c in plaintext:
        if c == '_':
            char_value = 1
        else:
            char_value = ord(c) - ord('a') + 2
        message = message * BASE + char_value
    return message

def decode(message):
    plaintext = ""
    while message > 0:
        r = message % BASE
        if r == 1:
            plaintext += '_'
        else:
            plaintext += chr(ord('a') + r - 2)
        message //= BASE
    return plaintext[::-1]

def invmod(x, p):
    return lgpow(x, p - 2, p);

def lgpow(a, b, mod):
    r = 1
    i = 1
    while i <= b:
        if i & b:
            r = r * a % mod
        a = a * a % mod
        i *= 2
    return r

class ElGamal:
    def __init__(self):
        f = open("prime.txt", 'r')
        self._p = int(f.read(), 16)
        self._g = 2
        self._a = random.randint(1, self._p - 2)
        self._ga = lgpow(self._g, self._a, self._p)

    def get_public_key(self):
        return [self._p, self._g, self._ga]

    def get_private_key(self):
        return self._a

    def encrypt(self, plaintext):
        message = encode(plaintext)
        print(message)
        k = random.randint(1, self._p - 2)
        alpha = lgpow(self._g, k, self._p)
        beta = message * lgpow(self._ga, k, self._p) % self._p
        return alpha, beta

    def decrypt(self, alpha, beta):
        message = lgpow(invmod(alpha, self._p), self._a, self._p) * beta % self._p
        print(message)
        return decode(message)
