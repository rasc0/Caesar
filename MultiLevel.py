# Multi-level encryption and decryption
import PythonAssignment as pa
while True:
    option = input("Would you like to encrypt or decrypt ('e' or 'd')?").lower()
    if option == 'e':
        encrypt = True
        break
    elif option == 'd':
        encrypt = False
        break
    else:
        print("Please type 'e' or 'd' ")

if encrypt:
    #gotta have a check to make sure that it is compatible (ascending order?)
    plaintext = input("What would you like to encrypt? ")
    keys = []
    ciphertext = ''
    keycount = int(input("How many keys would you like to use? "))
    for i in range(keycount):
    	key = input("Please input starting position and key 'x,y' ")
    	key = tuple(int(x) for x in key.split(","))
    	keys.append(key)
    for i in range(0,len(keys)-1):
        start, shift = keys[i]
        if i != len(keys):
            end, unimportant = keys[i+1]
        else:
            end = len(plaintext) - 1
        ciphertext += pa.cipher(shift, plaintext[start:end])
    print("Ciphertext is ", ciphertext)
        
#the decryption section (4), have to implement returning the keys in tuple form
elif not encrypt:
    ciphertext = input("What would you like to decrypt? ").lower()
    split = ciphertext.split()
    final = ''
    for word in split:
        for i in range(0, 25):
            pa.cipher(i, word)
            file = open("wordlistFull.txt", "r")
            lines = file.readlines()
            for line in lines:
                if line.lower() == word:
                    final += word + " "
                    break
    print("\nThe plaintext is: %s "% final)

