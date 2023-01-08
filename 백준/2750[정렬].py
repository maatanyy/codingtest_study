x = int(input())
array = []
for i in range(x):
    array.append(int(input()))

array.sort()

for i in range(len(array)):
    print(array[i])
