vals = int(input())

temps = [500,100,50,10]

count = 0

for i in temps:
    
    count+= (vals//i)
    vals = vals %i
    
print(count)