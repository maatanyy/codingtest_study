n, m = map(int,input().split())

baguni = [i for i in range(n+1)]


for _ in range(m):
    a, b = map(int,input().split())

    temp = baguni[a:b+1]
    temp.reverse()
    baguni[a:b+1] = temp

for i in range(1,n+1):
    print(baguni[i],end=' ')