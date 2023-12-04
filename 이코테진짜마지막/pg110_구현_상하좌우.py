num = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]
moving = ['L','R','U','D']

x , y = 1, 1

steps = input().split()

for step in steps:
    
    for k in range(len(moving)):
        
        if moving[k] == step:
            
            x+=dx[k]
            y+=dy[k]
            
            if x<1:
                x = 1
            if y>num:
                y=num
            if x>num:
                x=num
            if y<1:
                y = 1

print(x, y)
        