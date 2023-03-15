n = str(input())
length = (len(n))//2

sum1 = 0
sum2 = 0

for i in range(length):
    sum1 += int(n[i])

for i in range(length):
    sum2 += int(n[-(i+1)])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
