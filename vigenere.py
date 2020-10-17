CHARS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+`-=[]\\{}|;\':\",./<>? '

def encrypt(message,key):
    translated = []
    i=0
    
    for letter in message:
        num=CHARS.find(letter)
        if num != -1:
            num+=CHARS.find(key[i])
            num%=len(CHARS)
            translated.append(CHARS[num])

            i+=1
            if i==len(key):
                i=0   
        else:
            translated.append(letter)
    return ''.join(translated)

def decrypt(message,key):
    translated = []
    i=0
    
    for letter in message:
        num=CHARS.find(letter)
        if num != -1:
            num-=CHARS.find(key[i])
            num%=len(CHARS)            
            translated.append(CHARS[num])

            i+=1
            if i==len(key):
                i=0
        else:
            translated.append(letter)
    return ''.join(translated)