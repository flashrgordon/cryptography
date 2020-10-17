SYMBOLS='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+`-=[]\\{}|;\':\",./<>? '

def encrypt(n, message):
    ciphertext = ''
    notFound=0
    
    for letter in message:
        letter=letter
        if letter in SYMBOLS:
            letterIndex = SYMBOLS.find(letter)
            
            translatedIndex=letterIndex+n
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex<0:
                translatedIndex=translatedIndex+len(SYMBOLS)
                
            ciphertext=ciphertext+SYMBOLS[translatedIndex % len(SYMBOLS)]
            
        else:
            notFound+=1
            ciphertext= ciphertext + letter
    
    if notFound != 0:
        print(notFound, 'character(s) not encrypted because they are not in the list of allowable characters.')        

    return ciphertext

def decrypt(n, message):
    plaintext = ''
    notFound=0
    
    for letter in message:
        letter=letter
        if letter in SYMBOLS:
            letterIndex = SYMBOLS.find(letter)
            
            translatedIndex=letterIndex -n
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex<0:
                translatedIndex=translatedIndex +len(SYMBOLS)
                
            plaintext=plaintext+SYMBOLS[translatedIndex %len(SYMBOLS)]
            
        else:
            notFound+=1
            plaintext= plaintext + letter
            
    if notFound != 0:
        print(notFound, 'character(s) not decrypted because they are not in the list of allowable characters.')
            
    return plaintext