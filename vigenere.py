def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def encryption(string, key): 
  string = string.upper()
  encrypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text)) 

def decryption(encrypt_text, key): 
  encrypt_text = encrypt_text.upper()
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 

# File
def encrypt_file(file, keyword):
    #file_path = input("Enter File path : ")
    try:
        file1 = open(file, 'r+')
        f2 = open(file, 'w')
        print("File opened Successfully!!")
        file_data = file1.read()
        print("File read Successfully!!")
        key = generateKey(file_data, keyword)
        encrypted_data = encryption(file_data, key)
        f2.write(encrypted_data)
        print("Encrypted File stored on Desktop successfully!!")
 
    except Exception as e:
        print("Problems with opening the file")
        print(str(e))




if __name__ == "__main__":
    options = input("Jenis Masukannya Apa? Ketik 1 untuk file, ketik 2 untuk keyboard: ")
    if (options == "1"):
        file = input("Enter the filepath: ")
        keyword = input("Enter the keyword: ")
        encrypt_file(file, keyword)
    else:
        string = input("Enter the message: ")
        keyword = input("Enter the keyword: ")
        key = generateKey(string, keyword)
        encrypt_text = encryption(string,key)
        print("Encrypted message:", encrypt_text) 
        print("Decrypted message:", decryption(encrypt_text, key)) 
