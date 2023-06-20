values = input()

check = len(values)//2

temp1 = values[:check]
temp2 = values[check:]

sum1,sum2 = 0, 0

for i in temp1:
    sum1+=int(i)

for i in temp2:
    sum2+=int(i)

if sum1==sum2:
    print("LUCKY")
else:
    print("READY")