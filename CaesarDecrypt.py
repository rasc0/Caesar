import PythonAssignment as pa  # my custom library/module

lower_ascii_list = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
                    117, 118, 119, 120, 121,
                    122]

# The frequencies of each letter in the english language, used for calculating chi-squared score, numbers from Practical Cryptography
letter_frequencies = {"a": 8.55, "b": 1.60, "c": 3.16, "d": 3.87, "e": 12.1, "f": 2.18, "g": 2.09, "h": 4.96, "i": 7.33,
                      "j": 0.22, "k": 0.81, "l": 4.21, "m": 2.53, "n": 7.17, "o": 7.47, "p": 2.07, "q": 0.1, "r": 6.33,
                      "s": 6.73, "t": 8.94, "u": 2.68, "v": 1.06, "w": 1.83, "x": 0.19, "y": 1.72, "z": 0.11}

while True:
    try:
        print(
            "Method 1 - Print all possible key shifts \nMethod 2 - Use the Chi-Sqaured formula to print the most likely key shift (alphabetic characters only) \nMethod 3 - Compare words to known words in the english language")
        method = int(input("\nWould you like to use method 1 or method 2 or method 3? "))
        if method == 1 or method == 2:
            break
        elif method == 3:
            break
        else:
            print("please input '1', '2' or '3' ")
    except ValueError:
        print("please input '1', '2' or '3' ")

ciphertext = str(input("What is the ciphertext? "))

if method == 1:
    # which prints out all possible key shifts for the user to determine
    for i in range(26):
        plaintext = pa.cipher(i, ciphertext)
        print("\nShift: %s, Output: \n %s" % (str(i), plaintext))

elif method == 2:
    # chi-squared method:
    lowestChi = None  # starts as none, but then is given whatever the lowest (closest) chi-score is
    final = ''
    finalkey = 0
    for i in range(0, 25):
        plaintext = ''
        pa.rotate(1, lower_ascii_list)

        for letter in ciphertext.lower():
            if letter == " ":
                plaintext += " "
            elif letter.isalpha():
                index = ord(letter) - 97
                plaintext += str(chr(lower_ascii_list[index]))
            else:
                plaintext += ""

        chiscore = 0

        for letter in lower_ascii_list:
            letter = str(chr(letter))
            count = plaintext.count(letter)
            frequency = letter_frequencies[letter]
            expected = len(ciphertext) * frequency
            chiscore += ((count - expected) ** 2) / expected

        if lowestChi is None:
            lowestChi = chiscore
            final = plaintext
            finalkey = i
        else:
            if chiscore < lowestChi:
                lowestChi = chiscore
                final = plaintext
                finalkey = i

    print("\n with a chi-score of %d and a shift-key of %d, the message is %s" % (lowestChi, finalkey, final))

elif method == 3:
    # comparing to word list
    # determine how many "words" are in the ciphertext:
    ciphertext = ciphertext.lower()
    for i in range(0, 25):
        possible = ''
        count = 0
        plaintext = pa.cipher(i, ciphertext)
        split = plaintext.split()
        words = len(split)
        file = open("wordlistFull.txt", "r")
        lines = file.readlines()
        for line in lines:
            for word in split:
                if word == line.strip("\n").lower():
                    count += 1
        if count == words:
            print("the plaintext is: ", plaintext)