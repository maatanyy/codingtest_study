
arr = []

for i in range(8):
    x = int(input())
    arr.append([i+1,x])

arr.sort(key=lambda x:-x[1])


temp = []
ans = 0
for i in range(5):
    ans += arr[i][1]
    temp.append(arr[i][0])

temp.sort()
print(ans)
for i in temp:
    print(i,end=' ')