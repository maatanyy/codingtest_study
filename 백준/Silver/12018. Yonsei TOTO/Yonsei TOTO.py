num, ma = map(int,input().split())

values = []
count = 0

for i in range(num):
    num, person = map(int,input().split())
    temp = list(map(int,input().split()))

    if len(temp)<person:
        if ma > 0:
            count += 1
            ma = ma - 1
    else:
        values.append([temp,person])


for vals in values:
    vals[0].sort(reverse=True)

tempyo = []

for vals,t in values:
    tempyo.append(vals[t-1])

tempyo.sort()
i = 0
#print(tempyo)
for i in range(len(tempyo)):
    if ma>=tempyo[i]:
        count += 1
        ma = ma-tempyo[i]
    else:
        break

print(count)