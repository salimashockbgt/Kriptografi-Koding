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

def encryptByteExtendedVigenere(bytePlainText, key):
    result = [[0] for i in range(len(bytePlainText))]
    key = key.strip().upper()
    keyIndex = 0
    keylength = len(key)
    for i in range(len(bytePlainText)):
        keyIndex = keyIndex % keylength
        shift = ord(key[keyIndex]) - 65
        result[i] = bytes([(ord(bytePlainText[i]) + shift) % 256])
        keyIndex+=1
    return result

def decryptByteExtendedVigenere(byteCipherText, key):
    result = [[0] for i in range(len(byteCipherText))]
    key = key.strip().upper()
    keyIndex = 0
    keylength = len(key)
    for i in range(len(byteCipherText)):
        keyIndex = keyIndex % keylength
        shift = ord(key[keyIndex]) - 65
        result[i] = bytes([(ord(byteCipherText[i]) + 256 - shift) % 256]).decode("utf-8")
        keyIndex+=1
    return result

def write_to_file(path, text):
    file1 = open(path,"w+") 
    file1.write(text) 
    file1.close()

def readTextFromFile(path):
    file1 = open(path, "r")
    data = file1.read()
    file1.close()
    return data

data = readTextFromFile("plainText/text.txt")
print(data)
encrypt = encryptByteExtendedVigenere(data, "sony")
print(encryptByteExtendedVigenere(data, "sony"))
print(decryptByteExtendedVigenere(encrypt, "sony"))
decrypt = "".join(decryptByteExtendedVigenere(encrypt, "sony"))
write_to_file("cipherText/hasil.txt", decrypt)
