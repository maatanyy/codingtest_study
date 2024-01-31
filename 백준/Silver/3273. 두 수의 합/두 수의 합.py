num = int(input())

temp = list(map(int,input().split()))

temp.sort()


target = int(input())

start = 0
end = len(temp)-1

count = 0

while True:

    if start==end:
        break

    if temp[start] + temp[end] ==target:
        count+=1
        start+=1

    elif temp[start] + temp[end] <target:
        start+=1

    elif temp[start] + temp[end] > target:
        end-=1

print(count)