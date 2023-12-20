num = int(input())
temps = list(map(int, input().split()))
print(temps)
ans = [0] * (num+1)

ans[1] = temps[0]
ans[2] = max(temps[0],temps[1])

for i in range(3, num+1):

    ans[i] = max(ans[i-2]+temps[i-1], ans[i-1])

print(max(ans))



