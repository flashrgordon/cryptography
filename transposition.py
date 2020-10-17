import math

def encrypt(key, plaintext):
    ciphertext=['']*key
    
    for col in range(key):
        i=col
        
        while i<len(plaintext):
            ciphertext[col]+=plaintext[i]
            i+=key
            
    return ''.join(ciphertext)

def decrypt(key, ciphertext):
    cols=int(math.ceil(len(ciphertext)/key))
    rows=key
    omitted=(cols*rows)-len(ciphertext)
    plaintext=[''] *cols
    
    i=0 ##current column
    j=0 ##current row
    
    for letter in ciphertext:
        plaintext[i]+=letter
        i=i+1
        
        if (i==cols or (i==cols-1 and j >= rows-omitted)):
            i=0
            j=j+1
            
    return ''.join(plaintext)