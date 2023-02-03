#men-generate kunci sehingga jumlah huruf kunci sama dengan jumlah huruf masukan
def generateKey(text, key): 
  key = list(key) 
  if len(text) == len(key): 
    return(key) 
  else: 
    for i in range(len(text) - len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 

#melakukan enkripsi terhadap teks
def encryption(text, key): 
  text = text.upper()
  encrypt_text = [] 
  for i in range(len(text)): 
    x = (ord(text[i]) + ord(key[i])) % 26
    x = x + ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text)) 
#melakukan dekripsi terhadap teks yang telah dienkripsi
def decryption(encrypt_text, key): 
  encrypt_text = encrypt_text.upper()
  plaintext = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
    x = x + ord('A') 
    plaintext.append(chr(x)) 
  return("" . join(plaintext))
