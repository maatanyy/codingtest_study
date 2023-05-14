import sys

x = int(input())

temp = list(map(int,input().split()))

temp.sort()

y = int(input())

start= 0
end = len(temp)-1
count = 0

while start<end:
    if temp[start] + temp[end] < y:
        start+=1

    elif temp[start] + temp[end]==y:
        count+=1
        start+=1


    elif temp[start] + temp[end] > y:
        end = end-1

print(count)