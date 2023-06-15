temp = input()

val = ord(temp[0])-ord('a')+1
val2 = temp[1]

nx = [1, 1, 2, 2, -1, -1, -2, -2]
ny = [2, -2, 1, -1, 2, -2, 1, -1]

count = 0

for i in range(len(nx)):
    newX = int(val) + nx[i]
    newY = int(val2) + ny[i]

    if newX<1 or newX> 8 or newY<1 or newY>8:
        continue

    count+=1

print(count)

