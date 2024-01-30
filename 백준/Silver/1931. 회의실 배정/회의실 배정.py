import sys


num = int(input())

temp = []

for _ in range(num):
    temp.append(list(map(int,sys.stdin.readline().split())))

temp.sort(key= lambda x:(x[1],x[0]))


end = -1
count = 0

for i in temp:

    if i[0] >= end:
        end = i[1]
        count +=1


print(count)    