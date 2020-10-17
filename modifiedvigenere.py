import caesarcipher as caesar        

CHARS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+`-=[]\\{}|;\':\",./<>? '

def encrypt(message,key,seed):
    newKey=(getNewKey(seed,key,len(message))).upper()
  #  newChars=getNewChars(seed)
    translated = []
    i=0
    newKey=newKey.upper()
    
    for letter in message:
        num=CHARS.find(letter)
        if num != -1:
            num+=CHARS.find(newKey[i])
            num%=len(CHARS)
            translated.append(CHARS[num])

            i+=1
            if i==len(newKey):
                i=0
                
        else:
            translated.append(letter)
    return ''.join(translated)

def decrypt(message,key,seed):
    newKey=(getNewKey(seed,key,len(message))).upper()
   # newChars=getNewChars(seed)
    translated = []
    i=0
    newKey=newKey.upper()
    
    for letter in message:
        num=CHARS.find(letter)
        if num != -1:
            num-=CHARS.find(newKey[i])
            num%=len(CHARS)            
            translated.append(CHARS[num])

            i+=1
            if i==len(newKey):
                i=0
                
        else:
            translated.append(letter)
    return ''.join(translated)


# encrypts the key with a block size of len(key) and an unpredictable rotating caesar
# cipher based on user seed input, resulting in a new key of size len(message).
# vigenere ciphers are vulnerable to frequency analysis, especially with short keys.
# this modified vigenere cipher resolves that by generating a new key of the maximum
# effective length.
def getNewKey(seed,key,length):
    newKey=''
    i=1
  #  print('Old key:', key)
    while len(newKey) < length:
        newKey+=caesar.encrypt(int(seed)+((i*2)+1),key)
        i+=seed+1

    return newKey[:length]

def getNewChars(seed):
    return caesar.encrypt(seed, CHARS)