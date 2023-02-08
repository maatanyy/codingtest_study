answer = 0
n = 5
lost = [2, 4]
reserve = [3]

save = dict()
for i in range(1, n+1):
    save[i] = 1

for j in lost:
    save[j] -= 1

for k in reserve:
    save[k] += 1

for i in range(1, n+1):
    if save[i] == 2:
        if i == 1:
            if save[i+1]==0:
                save[i]=1
                save[i+1]=1
        elif i ==n:
            if save[i-1]==0:
                save[i-1]=1
                save[i]=1
        else:
            if save[i-1] == 0:
                save[i-1] = 1
                save[i] = 1
            elif save[i+1] == 0:
                save[i+1] = 1
                save[i] = 1

print(save)
for i in save.values():
    if i>=1:
        answer+=1

print(answer)
