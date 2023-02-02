# Extended Vigenere Cipher (256 Character ASCII)

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

def encrypt_Byte(bytePlainText, key):
    bytePlainText = str(bytePlainText)
    list_byte = list(bytePlainText)
    listed_key = list(key)

    # tempat hasil decrypt
    cipher_text = []

    for i in range(len(list_byte)):
        num_char = (ord(list_byte[i]) + ord(listed_key[i%len(key)])) % 256
        cipher_text.append(chr(num_char))

    return "".join(cipher_text).encode('utf-8')
    

def decrypt_Byte(byteCipherText, key):
    byteCipherText = str(byteCipherText)
    list_byte = list(byteCipherText)
    listed_key = list(key)

    # tempat hasil decrypt
    plain_text = []

    for i in range(len(list_byte)):
        num_char = (ord(list_byte[i]) - ord(listed_key[i%len(key)]) + 256) % 256
        plain_text.append(chr(num_char))

    return "".join(plain_text).encode('utf-8')

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



'''
encrypt = encrypt_Byte(data, "sony")
print(encrypt_Byte(data, "sony"))
print(decrypt_Byte(encrypt, "sony"))
decrypt = "".join(decrypt_Byte(encrypt, "sony"))
write_to_file("cipherText/hasil.txt", decrypt)'''

