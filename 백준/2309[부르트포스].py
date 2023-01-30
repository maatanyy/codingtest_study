# 리스트 인덱스 제거하는 법만 복습필요 나머지는 쉽게 풀었다. remove(값), 인덱스 요소는 del arr[x]
arr = []

for i in range(9):
    arr.append(int(input()))

arr.sort()

sum = 0
for i in range(9):
    sum += arr[i]

find = sum-100

def fi():
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j]==find:
                return arr[i],arr[j]

x, y = fi()
arr.remove(x)
arr.remove(y)


for i in arr:
    print(i)