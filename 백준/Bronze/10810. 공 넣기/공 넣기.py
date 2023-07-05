n, m  = map(int,input().split())

baguni = [0]*(n+1)
#print(baguni)
for _ in range(m):
    a, b, c = map(int, input().split())

    for j in range(a,b+1):
        baguni[j] = c


for i in range(1,n+1):
    print(baguni[i],end=' ')

