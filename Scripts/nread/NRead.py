SWidth = 42
decrypted_text = ""


array = []

password = input()
password = int(password[0]) - int(password[1])

StaticLen = len(array)
print("#:", StaticLen)


while True:

    try:
        Input = int(input())
    except ValueError:
        break

    if Input <= StaticLen and Input >= 1:
        Input -= 1  # Starts counting from 1 and not from 0

        if (
            array[Input][0] == -1
        ):  # Self formed text will contain -1 as the first element to indicate that this element doesn't needs modifcation
            for x in range(len(array[Input])):
                print(array[Input][x])

        else:
            for x in range(len(array[Input])):
                Pieces = (len(array[Input][x]) // SWidth) + 1
                for y in range(Pieces):
                    StartPoint = y * SWidth
                    EndPoint = StartPoint + SWidth

                    for x in range(len(array[Input][0][StartPoint:EndPoint])):
                        decrypted_text += chr(
                            ord(array[Input][0][StartPoint:EndPoint][x]) - password
                        )
                    print(decrypted_text)

                    decrypted_text = ""  # reset
    else:
        print("#", StaticLen)
