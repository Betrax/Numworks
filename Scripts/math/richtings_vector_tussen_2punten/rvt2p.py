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

vgl3 = []

for x in range(3):
    vgl3.append(vgl1[x] - vgl2[x])

print("R({}, {}, {})".format(vgl3[0], vgl3[1], vgl3[2]))
