n = str(input())

od = 0
ed = 0

for i in range(len(n)-1):
    if n[i] == '0' and n[i+1] == '1':
        od+=1
    elif n[i] == '1' and n[i+1] == '0':
        ed+=1

print(min(od,ed))