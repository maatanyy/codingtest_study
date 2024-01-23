def solution(command):    
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]] 
    x = 0  
    y = 0   
    dir = 0   
    
    for c in command:
        if c == 'R':
            dir = (dir+1)%4
        elif c == 'L':
            dir = (dir-1)%4
        elif c == 'G':
            x = x + dxy[dir][0]
            y = y + dxy[dir][1]
        elif c == 'B':
            x = x - dxy[dir][0]
            y = y - dxy[dir][1]
    
    return [x, y]