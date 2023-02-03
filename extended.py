# Extended Vigenere Cipher (256 Character ASCII)
from pathlib import Path

def extended_vigenere_encrypt(text, key):
    # convert text to list of char
    listed_text = list(text)
    listed_key = list(key)

    # tempat hasil encrypt
    encrypted_text = []

    for i in range(len(listed_text)):
        num_char = (ord(listed_text[i]) + ord(listed_key[i%len(key)])) % 256
        encrypted_text.append(chr(num_char))

    return ("".join(encrypted_text))

# print(extended_vigenere_encrypt("HALOGUYS123@gmail", "sony"))

def extended_vigenere_decrypt(encrypted_text, key):
    # convert text to list of char
    listed_encrypt_text = list(encrypted_text)
    listed_key = list(key)

    # tempat hasil decrypt
    plain_text = []

    for i in range(len(listed_encrypt_text)):
        num_char = (ord(listed_encrypt_text[i]) - ord(listed_key[i%len(key)]) + 256) % 256
        plain_text.append(chr(num_char))

    return ("".join(plain_text))

# print(extended_vigenere_decrypt("»°ºÈºÄÇÌ¤¡¡¹ÚÜÏâß", "sony"))


def write_to_file(path, text):
    file1 = open(path,"w+") 
    file1.write(text) 
    file1.close()

def readTextFromFile(path):
    file1 = open(path, "r")
    data = file1.read()
    file1.close()
    return data

def write_byte_file(filename, bytes):
    with open(filename, "wb") as binary_file:
        binary_file.write(bytes)

def open_byte_file(filename):
    with open(filename, 'rb') as f:
        contents = f.read()
        return contents

# untuk enkrip dan dekrip file sembarang
def enkripFile(path, key):
    file = open_byte_file(path)
    file = file.decode("ISO-8859-1")
    enkrip = extended_vigenere_encrypt(file, key)
    enkrip = enkrip.encode("ISO-8859-1")
    extension = Path(path).suffix
    write_byte_file("enkrip%s" % extension, enkrip)
    return ("enkrip%s" % extension)

def dekripFile(path, key):
    file = open_byte_file(path)
    file = file.decode("ISO-8859-1")
    dekrip = extended_vigenere_decrypt(file, key)
    dekrip = dekrip.encode("ISO-8859-1")
    extension = Path(path).suffix
    write_byte_file("dekrip%s" % extension, dekrip)
    return ("dekrip%s" % extension)

#print(Path('hasil.txt').suffix)

'''
file = open_byte_file("plainText/test.jpg")
file = file.decode("ISO-8859-1")
enkrip = extended_vigenere_encrypt(file, "sony")
enkrip = enkrip.encode("ISO-8859-1")
write_byte_file("hasil.jpg", enkrip)

file = open_byte_file("hasil.jpg")
file = file.decode("ISO-8859-1")
dekrip = extended_vigenere_decrypt(file, "sony")
dekrip = dekrip.encode("ISO-8859-1")
write_byte_file("hasilde.jpg", dekrip)
'''
'''
encrypt = encrypt_Byte(data, "sony")
print(encrypt_Byte(data, "sony"))
print(decrypt_Byte(encrypt, "sony"))
decrypt = "".join(decrypt_Byte(encrypt, "sony"))
write_to_file("cipherText/hasil.txt", decrypt)'''

