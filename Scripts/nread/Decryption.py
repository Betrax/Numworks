PASSWORD = 1

for x in range(9):
    x += 1
    File = "a ("+ str(x) +").txt"

    input_file = open(File, "r")
    Lines = input_file.readlines()
    text = ""

    for line in Lines:
        text = line.strip()
        decrypted_text = ""

        for x in range(len(text)):
            decrypted_text += chr(ord(text[x]) - PASSWORD)

        f = open(File, "a")
        f.write(decrypted_text + "\n")
        f.close()
