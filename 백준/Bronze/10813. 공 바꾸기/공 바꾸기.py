n, m = map(int,input().split())

baguni = [ i for i in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    temp1 = baguni[a]
    temp2 = baguni[b]
    baguni[a] = temp2
    baguni[b] = temp1

for i in range(1,n+1):
    print(baguni[i],end=' ')





















