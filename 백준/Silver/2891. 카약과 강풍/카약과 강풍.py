num, damage, one = map(int, input().split())

values = [1]*(num+1)

damages = map(int, input().split())
for j in damages:
    values[j]-=1

vals = map(int, input().split())

for i in vals:
    values[i]+=1

values = values[1:]

edge = len(values)
for i in range(0, edge):
    if values[i] == 0:
        if i == 0:
            if values[i+1] == 2:
                values[i+1] = 1
                values[i] = 1

        elif i == len(values) - 1:
            if values[i-1] == 2:
                values[i-1] = 1
                values[i] = 1
        else:
            if values[i-1] == 2:
                values[i-1] = 1
                values[i] = 1
                continue

            if values[i+1] == 2:
                values[i+1] = 1
                values[i] = 1
                continue
    else:
        continue


ans = values.count(0)
print(ans)

#2 0 2 0 2


