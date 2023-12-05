inp= input()

steps = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

x = int(ord('a')-ord(inp[0]))+1
y = int(inp[1])

count = 0

for i in steps:
    
    newX = x + i[0]
    newY = y + i[1]
    
    if 1<=newX <=8 and 1<=newY <=8:
        count+=1
        
print(count)