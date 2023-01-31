from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return '''
    <h1> Ragam Cipher Klasik</h1>
    <h2> by Ima & Shely </h2>
    <h3> Pilih metode cipher di bawah ini untuk Enkripsi & Dekripsi </h3>
    <p><a href="vigenere">Vigenere Cipher (26 Alphabet)</a></p>
    <p><a href="extendedVigenere">Extended Vigenere Cipher (256 char ASCII)</a></p>
    <p><a href="fairplay">Fairplay Cipher (26 Alphabet)</a></p>
    <p><a href="oneTimePad">One Time Pad Cipher (26 Alphabet)</a></p>
    '''

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    if request.method == 'POST':
        # disini perhitungan enkrip/ dekrip nya
        return '''
        <h1> Vigenere Chiper (26 Alphabet) </h1>
        <p style="color:red;">Catatan : Masukan plain text dan key tanpa spasi untuk melakukan enkripsi dan dekripsi.</p>
        
        <form action="vigenere" method="POST">
        <h2> Enkripsi </h2>
        <h3> Plain Text </h3>
        <input name = "plain_text">
        <h3> Key </h3>
        <input name = "key">
        <input type="submit" value="Enkripsi"/></form>

        <h3> Hasil Enkripsi : </h3>
        <p style="color:blue;"> hasil lalalala </p>

        <form action="vigenere" method="POST">
        <h2> Dekripsi </h2>
        <h3> Cipher Text </h3>
        <input name = "cipher_text">
        <h3> Key </h3>
        <input name = "key">
        <input type="submit" value="Dekripsi"/></form>

        <h3> Hasil Dekripsi : </h3>
        <p style="color:blue;"> hasil lalalala </p>
        '''
    else:
        return '''
        
        <h1> Vigenere Chiper (26 Alphabet) </h1>
        <p style="color:red;">Catatan : Masukan plain text dan key tanpa spasi untuk melakukan enkripsi dan dekripsi.</p>
        
        <form action="vigenere" method="POST">
        <h2> Enkripsi </h2>
        <h3> Plain Text </h3>
        <input name = "plain_text">
        <h3> Key </h3>
        <input name = "key">
        <input type="submit" value="Enkripsi"/></form>
        <h3> Hasil Enkripsi : </h3>

        <form action="vigenere" method="POST">
        <h2> Dekripsi </h2>
        <h3> Cipher Text </h3>
        <input name = "cipher_text">
        <h3> Key </h3>
        <input name = "key">
        <input type="submit" value="Dekripsi"/></form>
        <h3> Hasil Dekripsi : </h3>
        '''

if __name__ == '__main__':
    app.run(debug=True)