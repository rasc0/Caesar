# rotate an array n times:
def rotate(n, array):
    for i in range(0, n):
        # the next lines of code are to rotate an array ONE time, hence the for loop above
        first = array[0]

        for j in range(0, len(
                array) - 1):  # Removes the first object and shifts each object one index to the left ( 0 -> B)
            array[j] = array[j + 1]

        array[len(array) - 1] = first  # moves what was the first character to the end


def cipher(key, plaintext):
    # Array for the lowercase alphabet in ASCII form, this is what will be rotated

    lower_ascii_list = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
                        117, 118, 119, 120, 121,
                        122]
    upper_ascii_list = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
                        89,
                        90]
    specialChar_ascii_list = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
                              54,
                              55,
                              56, 57, 58, 59, 60, 61, 62, 63, 64]
    # rotate the ascii lists as many times as the key dictates:

    rotate(key, lower_ascii_list)
    rotate(key, upper_ascii_list)
    rotate(key, specialChar_ascii_list)

    ciphertext = ''

    for letter in plaintext:
        if letter == " ":
            ciphertext += " "
        elif letter.islower():
            index = ord(letter) - 97
            ciphertext += str(chr(lower_ascii_list[index]))
        elif letter.isupper():
            index = ord(letter) - 65
            ciphertext += str(chr(upper_ascii_list[index]))
        elif not letter.isalpha():  # if the letter is the message isn't an alphabetic character
            index = ord(letter) - 33
            ciphertext += str(chr(specialChar_ascii_list[index]))

    return ciphertext
