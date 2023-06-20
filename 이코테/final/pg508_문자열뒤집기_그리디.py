values = input()
length = len(values)-2

sum1 = 0
sum2 = 0

for i in range(length):
    if int(values[i])==0 and int(values[i+1])==1:
        sum1+=1
    elif int(values[i])==1 and int(values[i+1])==0:
        sum2+=1

print(min(sum1,sum2))

