num = int(input())

temp = []

for i in range(num):
    values = list(input().split())
    values[1] = int(values[1])
    values[2] = int(values[2])
    values[3] = int(values[3])
    temp.append(values)

temp.sort(key= lambda x:(x[3],x[2],x[1]))

print(temp[-1][0])
print(temp[0][0])