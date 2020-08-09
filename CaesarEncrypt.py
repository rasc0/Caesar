import re  # "re" is short for regex, a library used for checking strings and finding patterns in strings, for this I am
# using it to ensure that the input does not contain any special characters
import PythonAssignment as pa  # my custom library/module
import random

# Caesar Cipher:
while True:
    message = str(input("Message to be encrypted: "))  # input to determine what the user wants to encrypt
    regex = re.compile("[_^}{~]")
    if regex.search(message) is None:  # searches the input for the characters I have not included
        break
    else:
        print("please do not use any of the following characters: @_^}{~")

while True:
    key = int(input("How many movements (type 0 [zero] for random): "))  # this is the key which determines how many
    # keys to rotate
    if key == 0:  # generate a random key
        key = random.randint(1, 27)
        break
    elif key is None:
        print("Please put in a key.")
    else:
        break

ciphertext = pa.cipher(key, message)

print("The ciphertext is: \n %s" % ciphertext)
