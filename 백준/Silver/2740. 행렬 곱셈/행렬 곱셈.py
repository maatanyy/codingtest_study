import sys

n, m = map(int, input().split())

arr1 =[]

for _ in range(n):
    arr1.append(list(map(int, input().split())))

n2, m2 = map(int, input().split())

arr2 = []

for _ in range(n2):
    arr2.append(list(map(int, input().split())))

arr3 = [[0]*(m2) for _ in range(n)]


for i in range(len(arr1)):
    for j in range(len(arr2[0])):
        for k in range(len(arr1[0])):
            arr3[i][j] += arr1[i][k] * arr2[k][j]

for i in range(len(arr3)):
    for k in range(len(arr3[0])):
        print(arr3[i][k],end=' ')
    print()