# Playfair Cipher (26 character alphabet)

import numpy as np
import re

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# menyesuaikan text yang diinput
def process_text(text):
	process_text = re.sub(r"[^a-zA-Z]", '', text)
	process_text = process_text.upper()
	return process_text

# membuat kotak 5x5 tabel kunci
def generate_keytable(key):
	keytable = [['' for y in range(5)] for x in range(5)]
	key = process_text(key)
	key = re.sub(r"[J]", '', key)
	key = ''.join([j for i, j, in enumerate(key) if j not in key[:i]])
	key = key + re.sub(rf"[{key + 'J'}]", '', alphabet)
	for i in range(5) :
		for j in range(5) :
			keytable[i][j] = key[i*5 + j]
			keytable = np.array(keytable)
	return keytable

def encrypt_playfair(plainText, key):
	plainText = process_text(plainText)
	keytable = generate_keytable(key)

	cipherText = ''
	new_plainText = ''
	# membuat bigram
	if len(plainText) < 2:
		new_plainText = plainText
	else:
		for i in range(len(plainText)-1):
			new_plainText += plainText[i]
			if plainText[i] == plainText[i+1]:
				new_plainText += 'X'
		new_plainText += plainText[-1]
	
	if len(new_plainText) & 1:
		new_plainText += 'X'
	
	for i in range(0, len(new_plainText), 2):
		row1, col1 = np.where(keytable == new_plainText[i])
		row2, col2 = np.where(keytable == new_plainText[i+1])
		if row1 == row2:
			cipherText += keytable[row1][0][(col1+1) % 5][0]
			cipherText += keytable[row2][0][(col2+1) % 5][0]
		elif col1 == col2:
			cipherText += keytable[(row1+1) % 5][0][col1][0]
			cipherText += keytable[(row2+1) % 5][0][col2][0]
		else:
			cipherText += keytable[row1][0][col2][0]
			cipherText += keytable[row2][0][col1][0]
	
	return cipherText

def decrypt_playfair(cipherText, key):
	cipherText = process_text(cipherText)
	keytable = generate_keytable(key)

	plainText = ''

	for i in range(0, len(cipherText), 2):
		row1, col1 = np.where(keytable == cipherText[i])
		row2, col2 = np.where(keytable == cipherText[i+1])
		if row1 == row2:
			plainText += keytable[row1][0][(col1-1) % 5][0]
			plainText += keytable[row2][0][(col2-1) % 5][0]
		elif col1 == col2:
			plainText += keytable[(row1-1) % 5][0][col1][0]
			plainText += keytable[(row2-1) % 5][0][col2][0]
		else:
			plainText += keytable[row1][0][col2][0]
			plainText += keytable[row2][0][col1][0]
	
	plainText = re.sub(r"[X]", '', plainText)

	return plainText
	
'''
# tes
plaintext = "temui ibu nanti malam"
key = "jalan ganesha sepuluh"
enkrip = encrypt_playfair(plaintext, key)
print(enkrip)
dekrip = decrypt_playfair(enkrip, key)
print(dekrip)'''