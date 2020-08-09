with open("wordlist.txt", "r") as f:
    lines = f.readlines()
with open("wordlist.txt", "w") as f:
    for line in lines:
        if len(line.strip("\n")) <= 6:
            f.write(line)
