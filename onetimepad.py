from os import listdir, path
from random import seed, randint

def readTextFromFile(path):
    file1 = open(path, "r")
    data = file1.read()
    file1.close()
    return data

wordCollection = readTextFromFile('C:/Users/Lenovo/kripto/abc.txt')
#Menghasilkan kunci yang di-randomize secara acak
def generateKey(text):
    key = ''
    for i in range(len(text)):
        seed()
        key += wordCollection[randint(0,26)]
    return key
def geserHuruf(letter, shift):
    newIdx = wordCollection.index(letter) + shift
    if newIdx >= 27:
        return wordCollection[newIdx-27]
    elif newIdx >= 0 and newIdx < 27:
       return wordCollection[newIdx]
    else:
        return wordCollection[27+newIdx]

def crypto(text, key, cipher):
    keyShifts = []
    if cipher:
        # Mengubah huruf-huruf pada wordCollection menjadi koleksi urutan setiap huruf yang dikurangi 1
        for i in range(len(key)):
            keyShifts.append(wordCollection.index(key[i]) - wordCollection.index('a'))
    else:
        # sama seperti kondisi if, tetapi dalam bentuk negatif
        keyShifts = [ ((wordCollection.index(key[i]) - wordCollection.index('a')) * -1) for i in range(len(key)) ]
    textLetters=[]
    cipherKey=[]
    for i in range(len(text)):
        textLetters.append(text[i])
    # memasukkan setiap karakter dalam text menjadi array of strings
    # mengulang keyShifts supaya bisa dicocokkan dengan textLetters length ('hello' dengan key 'gk' akan menghasilkan [6, 10, 6, 10, 6])

    cipherKey = [ keyShifts[i % len(keyShifts)] for i in range(len(textLetters)) ]
    onetimepadText = [ geserHuruf(textLetters[i], cipherKey[i]) for i in range(len(textLetters)) ]   
    # shift every letter to encrypt/decrypt text

    return ''.join(onetimepadText)
