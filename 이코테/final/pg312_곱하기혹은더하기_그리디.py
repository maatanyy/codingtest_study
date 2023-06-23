values = input()

sumval = int(values[0])

for i in range(len(values)-1):
    if int(values[i])==0 or int(values[i])==1 or int(values[i+1])==0 or int(values[i+1])==1:
        sumval += int(values[i])+int(values[i+1])
    else:
        sumval *= int(values[i+1])

print(sumval)