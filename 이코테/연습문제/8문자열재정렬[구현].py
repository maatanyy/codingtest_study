data = input()

result =[]
sum =0

for i in data:
    if i.isalpha():
        result.append(i)
    else:
        sum+=int(i)

result.sort()

if sum!=0:
    result.append(str(sum))

print(''.join(result))