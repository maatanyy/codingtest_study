x = int(input())

money = 1000-x
count=0

arrays = [500,100,50,10,5,1]

for i in arrays:
    if money // i > 0 :
        count = count + money // i
        money = money%i

print(count)