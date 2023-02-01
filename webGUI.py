import os
from flask import *
from werkzeug.utils import secure_filename
from utils import *
import extended
import vigenere
app = Flask(__name__)

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        method = request.form.get('method')
        action = request.form.get('action')
        text = request.form['text']
        key = request.form['key']

        if method == "Extended Vigenere" and action == "Encrypt":
            return extended.extended_vigenere_encrypt(text, key)
        elif method == "Extended Vigenere" and action == "Decrypt":
            return extended.extended_vigenere_decrypt(text, key)
        elif method == "Vigenere" and action == "Encrypt":
            keyfix = vigenere.generateKey(text, key)
            encrypt_text = vigenere.encryption(text,keyfix)
            return encrypt_text
        elif method == "Vigenere" and action == "Decrypt":
            keyfix = vigenere.generateKey(text, key)
            decrypt_text = vigenere.decryption(text,keyfix)
            return decrypt_text

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
        <option value="One Tipe Pad">One Tipe Pad</option>
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

        <h4> Hasil Teks : </h4>

        '''
#UPLOAD_FOLDER = 'C:\Users\UX334FL\Downloads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'log'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/file', methods=['GET', 'POST'])
def file():
    if request.method == 'POST':
        method = request.form.get('method')
        action = request.form.get('action')
        key = request.form['key']
        file = request.files['file']
        '''
        if request.method == 'POST':
        # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                uploads = os.path.join(current_app.root_path, "plainText")
                file.save(os.path.join(uploads, filename))
                return redirect(url_for(request.url,
                                        filename=filename))'''

    else:
        return'''<h1> Extended Vigenere Chiper (256 character ASCII) </h1>
            <form action="file" method = "POST">
            <label for="method">Choose cipher method :</label>
            <select name="method" id="method">
            <option value="Vigenere">Vigenere</option>
            <option value="Extended Vigenere">Extended Vigenere</option>
            <option value="Playfair">Playfair</option>
            <option value="One Tipe Pad">One Tipe Pad</option>
            </select>
            <label for="action">Choose action :</label>
            <select name="action" id="action">
            <option value="Encrypt">Encrypt</option>
            <option value="Decrypt">Decrypt</option>
            </select>
            <p><input type=file name=file autocomplete="off" required></p>
            <p><input name="key"></p>
            <p><input type="submit" value="Submit"></p>
            </form>'''

@app.route('/showfile/<path:filename>')
def showfile(filename):
    uploads = os.path.join(current_app.root_path, "plainText")
    return send_from_directory(directory=uploads, path=filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)