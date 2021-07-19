from math import *

while True:
    full_list = input("->")
    full_list = full_list.split(",")

    if len(full_list) >= 6:
        break
    print("Type 6 items, you typed", len(full_list))

vgl1 = full_list[0:3]
vgl2 = full_list[3:6]

for x in range(3):
    vgl1[x] = eval(vgl1[x])

for x in range(3):
    vgl2[x] = eval(vgl2[x])


dec_hoek = degrees(
    acos(
        abs(vgl1[0] * vgl2[0] + vgl1[1] * vgl2[1] + vgl1[2] * vgl2[2])
        / (
            sqrt((vgl1[0] ** 2) + (vgl1[1] ** 2) + (vgl1[2] ** 2))
            * sqrt((vgl2[0] ** 2) + (vgl2[1] ** 2) + (vgl2[2] ** 2))
        )
    )
)
print(dec_hoek)  # raw print

uur_hoek = dec_hoek // 1
dec_hoek -= uur_hoek

min_hoek = dec_hoek * 60 // 1
dec_hoek -= min_hoek / 60

sec_hoek = dec_hoek * 3600
print("{}, {}', {}''".format(int(uur_hoek), int(min_hoek), sec_hoek))
