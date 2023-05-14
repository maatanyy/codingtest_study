x, y = map(int, input().split())

val = list(input())

sum = 0

for i in range(len(val)):
    if val[i]=='P':
        for j in range(i-y, i+y+1):
            if j>=0 and j<len(val):
                if val[j]=='H':
                    val[j]='C'
                    sum+=1
                    break

print(sum)