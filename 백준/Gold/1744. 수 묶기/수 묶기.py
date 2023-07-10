num = int(input())

pos = []
neg = []
one = []
totalVal = 0

for i in range(num):
    a = int(input())

    if a==1:
        one.append(a)

    elif a>0:
        pos.append(a)

    else:
        neg.append(a)

pos.sort(reverse=True)
neg.sort()


if len(pos)%2==1:
    totalVal+=pos[len(pos)-1]

    for i in range(0,len(pos)-1,2):
        totalVal+= (pos[i]*pos[i+1])
else:
    for i in range(0,len(pos)-1,2):
        totalVal+= (pos[i]*pos[i+1])

if len(neg)%2==1:
    totalVal+=neg[len(neg)-1]

    for i in range(0,len(neg)-1,2):
        totalVal+=(neg[i]*neg[i+1])
else:
    for i in range(0,len(neg)-1,2):
        totalVal+=(neg[i]*neg[i+1])

for i in one:
    totalVal+=i

print(totalVal)







