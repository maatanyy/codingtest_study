values = input()

sum = 0
temp = []
for i in values:
    if i.isalpha():
        temp.append(i)
    else:
        sum+=int(i)

temp.sort()

temp.append(str(sum))

print(''.join(temp))