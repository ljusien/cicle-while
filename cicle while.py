l = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(l):
    print(l[index])
    index += 1
    if l[index] < 0:
        break
