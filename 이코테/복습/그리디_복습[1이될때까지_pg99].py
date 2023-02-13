x , y = map(int,input().split())

count = 0

while x!=1:
    if x%y==0:
        count+=1
        x=x//y
    else:
        x = x-1
        count+=1

print(count)