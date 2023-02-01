'''def generateKey(string, key): 
	key = list(key) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) - len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key)) 

def encryptText(plain_text, key):
    cipher = [[0] for i in range(len(plain_text))]
    key = generateKey(plain_text, key)
    key = key.strip().upper()
    keyIndex = 0
    for i in range (len(plain_text)):
        keyIndex = keyIndex % len(key)
        shift = ord(key[keyIndex]) - 65
        cipher[i] = chr((ord(plain_text[i]) + shift) % 256)
        keyIndex += 1
    return "".join(cipher)

print(encryptText("thisplaintext", "sony"))'''

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

print(extended_vigenere_encrypt("HALOGUYS123@gmail", "sony"))

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

print(extended_vigenere_decrypt("»°ºÈºÄÇÌ¤¡¡¹ÚÜÏâß", "sony"))