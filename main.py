# Author        Ryan Gordon
# Use           Cipher interface
# Last Edited   13 October 2020


import caesarcipher as caesar
import transposition as trans
import vigenere as vig
import modifiedvigenere as mvig

def main():
    answer=input('Would you like to perform a cipher operation? Enter y/n.\n')
    while answer.lower()=='y':
        print('1.) Caesar Cipher')
        print('2.) Transposition Cipher')
        print('3.) Classic Vigenere Cipher')
        print('4.) Modified Vigenere Cipher')
        print('5.) View Modified Vigenere Keys')
        print('0.) Exit')
        cipherChoice=input('Enter an option 0-5.\n')
        while not ((cipherChoice).isdigit() and int(cipherChoice) >= 0 and int(cipherChoice) <= 5):
            cipherChoice=str(input('\nInvalid entry. Enter an integer from 0-5.\n'))
        
        print('Your choice was', cipherChoice)         
        cipherChoice=int(cipherChoice)
        
        if cipherChoice != 0 and cipherChoice != 5:
            mode=input('Would you like to encrypt or decrypt? Enter e/d.\n')
            while not (mode.lower() == 'e' or mode.lower() =='d'):
                mode=input('Invalid entry. Enter e to encrypt or d to decrypt.\n')
        
        if cipherChoice==1:
            print('Caesar Cipher:')
            n=input('Enter the shift value n:\n')
            while not n.isdigit():
                n=input('Enter a valid integer.\n')
            n=int(n)
            
            if mode=='d':
                ciphertext=input('Enter the ciphertext.\n')
                plaintext=(caesar.decrypt(n,ciphertext))
                print('Ciphertext:\n', ciphertext)
                print('Plaintext:\n', plaintext)
            
            elif mode=='e':
                plaintext=input('Enter the plaintext.\n')
                ciphertext=(caesar.encrypt(n,plaintext))
                print('Plaintext:\n', plaintext)
                print('Ciphertext:\n', ciphertext)

        elif cipherChoice==2:
            print('Transposition Cipher:')
            key=input('Enter an integer key\n')
            while not key.isdigit():
                key=input('Key must be an integer.\n')
            key=int(key)
            
            if mode=='d':
                ciphertext=input('Enter the ciphertext.\n')
                plaintext=trans.decrypt(key,ciphertext)
                print('Ciphertext:\n',ciphertext)
                print('Plaintext:\n',plaintext)
            elif mode=='e':
                plaintext=input('Enter the plaintext.\n')
                ciphertext=trans.encrypt(key,plaintext)
                print('Plaintext:\n',plaintext)
                print('Ciphertext:\n',ciphertext)

        elif cipherChoice==3:
            print('Classic Vigenere Cipher:')
            key=input('Enter a key:\n')
            
            if mode=='d':
                ciphertext=input('Enter the ciphertext.\n')
                plaintext=vig.decrypt(ciphertext,key)
                print('Ciphertext:\n',ciphertext)
                print('Plaintext:\n',plaintext)
            elif mode=='e':
                plaintext=input('Enter the plaintext.\n')
                ciphertext=vig.encrypt(plaintext,key)
                print('Plaintext:\n',plaintext)
                print('Ciphertext:\n',ciphertext)
            
        elif cipherChoice==4:
            print('Modified Vigenere Cipher:')
            seed=input('Enter a positive seed value:\n')
            while not seed.isdigit():
                seed=input('Error, seed value must be a positive integer.\n')
            while int(seed) <= 0:
                print('Error, seed value must be positive. Exiting to main menu.')
                break
            seed=int(seed)
            key=input('Enter a key:\n')
            
            if mode=='d':
                ciphertext=input('Enter the ciphertext.\n')
                plaintext=mvig.decrypt(ciphertext,key,seed)
                print('Ciphertext:\n',ciphertext)
                print('Plaintext:\n',plaintext)
            elif mode=='e':
                plaintext=input('Enter the plaintext.\n')
                ciphertext=mvig.encrypt(plaintext,key,seed)
                print('Plaintext:\n',plaintext)
                print('Ciphertext:\n',ciphertext)
        
        elif cipherChoice==5:
            print('Modified Vigenere Keys:')
            seed=input('Enter a positive seed value:\n')
            while not seed.isdigit():
                seed=input('Error, seed value must be a positive integer.\n')
            while int(seed) <= 0:
                print('Error, seed value must be positive. Exiting to main menu.')
                break
            seed=int(seed)
            key=input('Enter a key:\n')
            message=input('Enter a message:\n')
            
            print('Entered key:',key)
            key=mvig.getNewKey(seed,key,len(message))
            print('Used key:',key)
            
        elif cipherChoice==0:
            print('Exiting now.')
            exit()


main()