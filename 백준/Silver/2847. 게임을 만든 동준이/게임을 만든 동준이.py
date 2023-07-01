num = int(input())

arr = []

for _ in range(num):
    arr.append(int(input()))

count = 0


for i in range(len(arr)-1,0,-1):
    while arr[i]<=arr[i-1]:
        arr[i-1]-=1
        count+=1

print(count)


