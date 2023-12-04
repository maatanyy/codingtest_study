n, m, k = map(int,input().split())

temps = list(map(int,input().split()))

temps.sort(reverse=True)
f1 = temps[0]
f2 = temps[1]

length = k
sumval = 0

while True:
    for i in range(k):
        if m==0:
            break
        
        sumval+=f1
        m-=1
    
    if m==0:
        break
    sumval +=f2
    m-=1
    
print(sumval)