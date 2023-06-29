from bisect import bisect_left
num = int(input())

for _ in range(num):
    values = list(map(int, input().split()))

    number = values[0]
    values = values[1:]

    step = 0
    temp = []

    for i in range(len(values)-1,0,-1):
        for j in range(i):
            if values[j]>values[j+1]:
                values[j],values[j+1] = values[j+1],values[j]
                step+=1

    print(number, step)







