x = int(input())

count = 0
val = x%5

if x==1 or x==3:
    count = -1

elif val%2==0:
    count = x//5 + val//2

else:
    count = ((x//5)-1+(val+5)//2)

print(count)



