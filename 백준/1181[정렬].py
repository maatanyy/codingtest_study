x = int(input())

array=[]
for i in range(x):
    array.append(str(input()))

array =list(set(array))

array.sort()
array.sort(key=lambda x: len(x))

for i in array:
    print(i)