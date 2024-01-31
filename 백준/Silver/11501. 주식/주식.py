import sys
testcase = int(input())

for _ in range(testcase):

    answer = 0

    day = int(input())
    temp = list(map(int,sys.stdin.readline().split()))
    
    first = temp[-1]

    for k in range(day-1,-1,-1):
        
        if temp[k] > first:
            first = temp[k]
        
        else:
            answer+= (first - temp[k])

        
    print(answer)