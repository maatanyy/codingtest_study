x , y = map(int, input().split())

array1 = list(map(int,input().split()))
array2 = list(map(int,input().split()))

array1.sort()
array2.sort(reverse=True)

for i in range(y):
    if array1[i]< array2[i]:
        array1[i], array2[i] = array2[i],array1[i]
    else:
        break

print(sum(array1))