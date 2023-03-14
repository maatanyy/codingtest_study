n = int(input())

val = list(map(int,input().split()))

val.sort()

result = 0

count = 0

for i in val:
    count+=1

    if count>=i:
        result+=1
        count=0

print(result)

