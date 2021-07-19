from math import *


def main():
    while True:
        full_list = input("->")
        full_list = full_list.split(",")

        if len(full_list) >= 6:
            break
        print("Type 6 items, you typed", len(full_list))

    vgl1 = full_list[0:3]
    vgl2 = full_list[3:6]

    print(
        "x*det([["
        + vgl1[1]
        + ","
        + vgl1[2]
        + "]["
        + vgl2[1]
        + ","
        + vgl2[2]
        + "]])-y*det([["
        + vgl1[0]
        + ","
        + vgl1[2]
        + "]["
        + vgl2[0]
        + ","
        + vgl2[2]
        + "]])+z*det([["
        + vgl1[0]
        + ","
        + vgl1[1]
        + "]["
        + vgl2[0]
        + ","
        + vgl2[1]
        + "]])"
    )

    for x in range(3):
        vgl1[x] = eval(vgl1[x])

    for x in range(3):
        vgl2[x] = eval(vgl2[x])

    print(
        vgl1[1] * vgl2[2] - vgl1[2] * vgl2[1],
        (vgl1[0] * vgl2[2] - (vgl1[2] * vgl2[0])) * -1,
        vgl1[0] * vgl2[1] - (vgl1[1] * vgl2[0]),
        "\n",
    )


main()
