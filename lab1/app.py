from flask import Flask, request, redirect, render_template, url_for, jsonify
from hill_cipher import HillCipher, det 

app = Flask(__name__)
app.jinja_env.auto_reload = True


def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a


def contains_only_characters_from(text, alphabet):
    for x in text:
        if x not in alphabet:
            return False
    return True


def is_good_alphabet(alphabet):
    d = {}
    for x in alphabet:
        if x not in d:
            d[x] = 0
        d[x] += 1
    for x in d.values():
        if x > 1:
            return False
    basic_alphabet = "_abcdefghijklmnopqrstuvwxyz"
    return contains_only_characters_from(alphabet, basic_alphabet)


@app.route('/')
def main():
    return render_template('index.html')


alphabet = "_abcdefghijklmnopqrstuvwxyz"
plaintext = "encode_this_text"
ciphertext = ""
key = [[1, 0], [0, 1]]

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    global alphabet
    global plaintext
    global ciphertext
    global key
    ciphertext = ""
    warning = ""
    if request.method == 'POST':
        alphabet = request.form['alphabet']
        plaintext = request.form['plaintext']
        a_0_0 = request.form['a_0_0']
        a_0_1 = request.form['a_0_1']
        a_1_0 = request.form['a_1_0']
        a_1_1 = request.form['a_1_1']
        n = len(alphabet)
        try: 
            a_0_0 = int(a_0_0)
            a_0_1 = int(a_0_1)
            a_1_0 = int(a_1_0)
            a_1_1 = int(a_1_1)
            key = [[a_0_0, a_0_1], [a_1_0, a_1_1]]
            if det(key) == 0:
                warning = "key must be invertible"
            elif gcd(n, det(key)) != 1:
                warning = "gcd(n, det(key)) must be 1"
            elif not is_good_alphabet(alphabet):
                warning = "Alphabet should contain only _ and [a-z] and no duplicates."
            elif not contains_only_characters_from(plaintext, alphabet):
                warning = "The text should contain only characters from the alphabet."
            else: 
                try:
                    cipher = HillCipher(range(n), range(n), key, alphabet)
                    ciphertext = cipher.encrypt(plaintext)
                except:
                    warning = "Only _ and [a-z] are allowed."
        except:
            warning = "Invalid key."
    return render_template('encrypt.html', \
            alphabet=alphabet, \
            plaintext=plaintext, \
            ciphertext=ciphertext, \
            a_0_0=key[0][0], \
            a_0_1=key[0][1], \
            a_1_0=key[1][0], \
            a_1_1=key[1][1], \
            warning=warning)


@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    global alphabet
    global plaintext
    global ciphertext
    global key
    plaintext = ""
    warning = ""
    if request.method == 'POST':
        alphabet = request.form['alphabet']
        ciphertext = request.form['ciphertext']
        a_0_0 = request.form['a_0_0']
        a_0_1 = request.form['a_0_1']
        a_1_0 = request.form['a_1_0']
        a_1_1 = request.form['a_1_1']
        n = len(alphabet)
        try: 
            a_0_0 = int(a_0_0)
            a_0_1 = int(a_0_1)
            a_1_0 = int(a_1_0)
            a_1_1 = int(a_1_1)
            key = [[a_0_0, a_0_1], [a_1_0, a_1_1]]
            if det(key) == 0:
                warning = "key must be invertible"
            elif gcd(n, det(key)) != 1:
                warning = "gcd(n, det(key)) must be 1"
            elif not is_good_alphabet(alphabet):
                warning = "Alphabet should contain only _ and [a-z] and no duplicates."
            elif not contains_only_characters_from(ciphertext, alphabet):
                warning = "The text should contain only characters from the alphabet."
            else: 
                try:
                    cipher = HillCipher(range(n), range(n), key, alphabet)
                    plaintext = cipher.decrypt(ciphertext)
                except:
                    warning = "Only _ and [a-z] are allowed."
        except:
            warning = "Invalid key."
    return render_template('decrypt.html', \
            alphabet=alphabet, \
            plaintext=plaintext, \
            ciphertext=ciphertext, \
            a_0_0=key[0][0], \
            a_0_1=key[0][1], \
            a_1_0=key[1][0], \
            a_1_1=key[1][1], \
            warning=warning)
