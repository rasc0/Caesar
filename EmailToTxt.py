import imaplib  # used to access an email inbox (IMAP = Internet Message Access Protocol)
import base64
# This is a program which will login to the user's email (if IMAP is enabled), read the email (encrypted)
# Then it will save it to a text file to make it easier to decrypt

imap_host = "imap.gmail.com"
imap_username = str(input("what is your email address? Please include the @gmail.com "))
imap_password = base64.b64encode(str(input("What is your email password? Don't worry, this will remain encrypted ")).encode("utf-8"))  # encoding the user's password with base64

imap = imaplib.IMAP4_SSL(imap_host)

imap.login(imap_username, base64.b64decode(imap_password))

file = open("email.txt", "w+")

imap.select("inbox"
            result, data = imap.uid('search', None, "ALL"))

    file.write(str(n))
    file.close()

