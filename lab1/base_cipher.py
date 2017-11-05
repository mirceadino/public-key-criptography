class Mapper:
    def __init__(self, keys="_abcdefghijklmnopqrstuvwxyz", values=range(0,27)):
        self.key_to_value = {}
        self.value_to_key = {}
        n = len(keys)
        for i in range(0, n):
            self.key_to_value[keys[i]] = values[i]
            self.value_to_key[values[i]] = keys[i]

    def text_to_code(self, text):
        """
        "abc" -> [0, 1, 2]
        """
        code = []
        for character in text:
            code.append(self.key_to_value[character])
        print(text, code)
        return code

    def code_to_text(self, code):
        """
        [0, 1, 2] -> "abc"
        """
        text = ""
        for character in code:
            text += self.value_to_key[character]
        print(code, text)
        return text


class BaseEncrypter:
    def __init__(self, plaintext, ciphertext, key):
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.key = key
        self.space = plaintext[0]

    def encrypt(self, text):
        return text


class BaseDecrypter:
    def __init__(self, plaintext, ciphertext, key):
        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.key = key
        self.space = plaintext[0]

    def decrypt(self, text):
        return text


class BaseCipher:
    def __init__(self, encrypter, decrypter, mapper=Mapper()):
        self.encrypter = encrypter
        self.decrypter = decrypter
        self.mapper = mapper

    def encrypt(self, text):
        initial = self.mapper.text_to_code(text)
        code = self.encrypter.encrypt(initial)
        final = self.mapper.code_to_text(code)
        return final

    def decrypt(self, text):
        initial = self.mapper.text_to_code(text)
        code = self.decrypter.decrypt(initial)
        final = self.mapper.code_to_text(code)
        return final


