x = int(input())
array = []
for i in range(x):
    array.append(int(input()))

for i in range(x):
    min_index = i
    for j in range(i+1,x):
        if array[j] < array[min_index]:
            min_index = j
    array[i],array[min_index] = array[min_index],array[i]

for i in range(len(array)):
    print(array[i])
