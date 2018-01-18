from flask import Flask, request, redirect, render_template, url_for, jsonify
from el_gamal import ElGamal

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


el_gamal = ElGamal()
plaintext = "encode_this_text"
public_key = el_gamal.get_public_key()
private_key = el_gamal.get_private_key()
alpha = 1
beta = 1

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    global el_gamal
    global plaintext
    global public_key
    global private_key
    global alpha
    global beta
    warning = ""
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        p = request.form['p']
        g = request.form['g']
        ga = request.form['ga']
        private_key = request.form['private_key']
        try: 
            p = int(p)
            g = int(g)
            ga = int(ga)
            public_key = [p, g, ga]
            private_key = int(private_key)
        except:
            warning = "Invalid public key."
        alpha, beta = el_gamal.encrypt(plaintext)
    return render_template('encrypt.html', \
            plaintext=plaintext, \
            p=public_key[0], \
            g=public_key[1], \
            ga=public_key[2], \
            private_key=private_key, \
            alpha=alpha, \
            beta=beta, \
            warning=warning)


@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    global el_gamal
    global plaintext
    global public_key
    global private_key
    global alpha
    global beta
    warning = ""
    if request.method == 'POST':
        plaintext = request.form['plaintext']
        p = request.form['p']
        g = request.form['g']
        ga = request.form['ga']
        alpha = request.form['alpha']
        beta = request.form['beta']
        try: 
            p = int(p)
            g = int(g)
            ga = int(ga)
            public_key = [p, g, ga]
            private_key = int(private_key)
            alpha = int(alpha)
            beta = int(beta)
        except:
            warning = "Invalid public key."
        plaintext = el_gamal.decrypt(alpha, beta)
    return render_template('decrypt.html', \
            plaintext=plaintext, \
            p=public_key[0], \
            g=public_key[1], \
            ga=public_key[2], \
            private_key=private_key, \
            alpha=alpha, \
            beta=beta, \
            warning=warning)

