list = []
while True:
    add = float(input("enter:"))
    if add == -1:
        break
    else:
        list.append(add)

total = sum(list)
print(total)
broekn = total / 12
print(broekn)
