val = str(input())

arr = []

for i in range(len(val)):
    arr.append(val[i:])

arr.sort()

for i in arr:
    print(i)