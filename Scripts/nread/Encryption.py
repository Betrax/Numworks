PASSWORD = 1

input_file = open("input.txt", "r")
Lines = input_file.readlines()
text = ""

for line in Lines:
    text = line.strip()
    decrypted_text = ""

    for x in range(len(text)):
        decrypted_text += chr(ord(text[x]) + PASSWORD)

    f = open("decryption.txt", "a")
    f.write("\"" + decrypted_text + "\",\n")
    f.close()
