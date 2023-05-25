num = int(input())

values = list(map(int,input().split()))
values.sort()
#print(values)
edge = len(values)
ans = []

for i in range(num):
    ans.append(values[i]+values[edge-1-i])

ans.sort()

minval  = ans[0]
print(minval)