n, m = map(int,input().split())

array = list(map(int, input().split()))
array.sort()

for i in range(n):
    if array[i]<=m:
        m+=1
    else:
        break

print(m)