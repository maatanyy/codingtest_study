total = int(input())
sum=0
num = int(input())

for i in range(num):
    a, b= map(int,input().split())
    sum +=a*b

if sum ==total:
    print('Yes')
else:
    print('No')