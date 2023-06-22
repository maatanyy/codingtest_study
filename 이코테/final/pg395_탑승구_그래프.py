from collections import deque
gate = int(input())

gates = [0] * (gate+1)
gates[0] = 1

plane = int(input())
planes = deque()

for _ in range(plane):
    planes.append(int(input()))

#print(planes)
count = 0

while True:
    x = planes.popleft()
    check = False
    count2 = 0
    for i in range(x,0,-1):
        if gates[i] == 0:
            gates[i] = 1
            count += 1
            break

        else:
            count2+=1

    if count2==x:
        break



print(count)








