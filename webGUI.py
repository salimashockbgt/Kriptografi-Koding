import os
from flask import *
from werkzeug.utils import secure_filename
from utils import *
import extended
import vigenere
import playfair
import onetimepad
app = Flask(__name__)

def write_to_file(path, text):
    file1 = open(path,"w+") 
    file1.write(text) 
    file1.close()

def readTextFromFile(path):
    file1 = open(path, "r")
    data = file1.read()
    file1.close()
    return data

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        method = request.form.get('method')
        action = request.form.get('action')
        text = request.form['text']
        key = request.form['key']
        # extended vigenere
        if method == "Extended Vigenere" and action == "Encrypt":
            return '<h3>Hasil encrypt : %s</h3>' % extended.extended_vigenere_encrypt(text, key)
        elif method == "Extended Vigenere" and action == "Decrypt":
            return '<h3>Hasil decrypt : %s</h3>' % extended.extended_vigenere_decrypt(text, key)
        # vigenere
        elif method == "Vigenere" and action == "Encrypt":
            keyfix = vigenere.generateKey(text, key)
            encrypt_text = vigenere.encryption(text,keyfix)
            return '<h3>Hasil encrypt : %s</h3>' % encrypt_text
        elif method == "Vigenere" and action == "Decrypt":
            keyfix = vigenere.generateKey(text, key)
            decrypt_text = vigenere.decryption(text,keyfix)
            return '<h3>Hasil decrypt : %s</h3>' % decrypt_text
        # playfair
        elif method == "Playfair" and action == "Encrypt":
            return '<h3>Hasil encrypt : %s</h3>' % playfair.encrypt_playfair(text, key)
        elif method == "Playfair" and action == "Decrypt":
            return '<h3>Hasil decrypt : %s</h3>' % playfair.decrypt_playfair(text, key)
        # One time pad
        elif method == "One Time Pad" and action == "Encrypt":
            otpkey = onetimepad.generateKey(text)
            return '<h3>Hasil encrypt : </h3>' + onetimepad.crypto(text, otpkey, True) + '\n<h3>Kunci: </h3>' + otpkey
        elif method == "One Time Pad" and action == "Decrypt":
            return '<h3>Hasil decrypt : %s</h3>' % onetimepad.crypto(text, key, False)

    else:
        return '''
        <h1> Ragam Cipher Klasik</h1>
        <h2> by Ima & Shely </h2>
        <p><a href="/file">Enkripsi & Dekripsi dengan File</a></p>
        <h3> Pilih metode cipher di bawah ini untuk Enkripsi & Dekripsi </h3>
        <form action="main" method = "POST">
        <label for="method">Choose cipher method :</label>
        <select name="method" id="method">
        <option value="Vigenere">Vigenere</option>
        <option value="Extended Vigenere">Extended Vigenere</option>
        <option value="Playfair">Playfair</option>
        <option value="One Time Pad">One Time Pad</option>
        </select>
        <label for="action">Choose action :</label>
        <select name="action" id="action">
        <option value="Encrypt">Encrypt</option>
        <option value="Decrypt">Decrypt</option>
        </select>
        <h4> Masukan Text </h4>
        <p><input name="text"></p>
        <h4> Masukan Key </h4>
        <p><input name="key"></p>
        <p><input type="submit" value="Submit"></p>
        </form>
        '''


@app.route('/file', methods=['GET', 'POST'])
def file():
    if request.method == 'POST':
        method = request.form.get('method')
        action = request.form.get('action')
        key = request.form['key']
        path = request.form['filename']

        isiFile = readTextFromFile(path)
        
        if method == "Vigenere" and action == "Encrypt":
            keyfix = vigenere.generateKey(isiFile, key)
            encrypt_text = vigenere.encryption(isiFile,keyfix)
            write_to_file("hasil.txt", encrypt_text)
        elif method == "Vigenere" and action == "Decrypt":
            keyfix = vigenere.generateKey(isiFile, key)
            decrypt_text = vigenere.decryption(isiFile,keyfix)
            write_to_file("hasil.txt", decrypt_text)
        elif method == "Extended Vigenere" and action == "Encrypt":
            encrypt_text = extended.extended_vigenere_encrypt(isiFile, key)
            write_to_file("hasil.txt", encrypt_text)
        elif method == "Extended Vigenere" and action == "Decrypt":
            decrypt_text = extended.extended_vigenere_decrypt(isiFile, key)
            write_to_file("hasil.txt", decrypt_text)
        elif method == "Playfair" and action == "Encrypt":
            encrypt_text = playfair.encrypt_playfair(isiFile, key)
            write_to_file("hasil.txt", encrypt_text)
        elif method == "Playfair" and action == "Decrypt":
            decrypt_text = playfair.decrypt_playfair(isiFile, key)
            write_to_file("hasil.txt", decrypt_text)
        elif method == "One Time Pad" and action == "Encrypt":
            encrypt_text = onetimepad.crypto(isiFile, onetimepad.generateKey(isiFile), True)
            write_to_file("hasil.txt", encrypt_text)
            write_to_file("key_onetimepad.txt", onetimepad.generateKey(isiFile))
        elif method == "One Time Pad" and action == "Decrypt":
            decrypt_text = onetimepad.crypto(isiFile, key, False)
            write_to_file("hasil.txt", decrypt_text)


        return redirect('/showfile/hasil.txt')

        

    else:
        return'''<h1> Extended Vigenere Chiper (256 character ASCII) </h1>
            <form action="file" method = "POST">
            <label for="method">Choose cipher method :</label>
            <select name="method" id="method">
            <option value="Vigenere">Vigenere</option>
            <option value="Extended Vigenere">Extended Vigenere</option>
            <option value="Playfair">Playfair</option>
            <option value="One Time Pad">One Time Pad</option>
            </select>
            <label for="action">Choose action :</label>
            <select name="action" id="action">
            <option value="Encrypt">Encrypt</option>
            <option value="Decrypt">Decrypt</option>
            </select>
            <h4> Masukan path file Anda </h4>
            <p><input name=filename required></p>
            <h4> Masukan Key/Filename </h4>
            <p><input name="key"></p>
            <p><input type="submit" value="Submit"></p>
            </form>'''

@app.route('/showfile/<path:filename>')
def showfile(filename):
    uploads = os.path.join(current_app.root_path, "")
    return send_from_directory(directory=uploads, path=filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
