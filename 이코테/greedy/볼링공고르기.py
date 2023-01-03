x, y = input().split()
ball = list(map(int, input().split()))

count =0

for i in range(len(ball)):
    for j in range(i+1,len(ball)):
        if ball[i]!=ball[j]:
            count+=1

print(count)