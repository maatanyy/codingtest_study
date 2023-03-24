arr = [0] * 9

for i in range(1,9):
    num = int(input())
    arr[i] = num

sum = 0
ans = []
for _ in range(5):
    temp = max(arr)
    sum += temp
    ans.append(arr.index(temp))
    arr[arr.index(temp)] = 0

ans.sort()
print(sum)
for i in ans:
    print(i,end=' ')

