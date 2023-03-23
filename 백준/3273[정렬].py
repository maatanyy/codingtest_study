# 시간 초과 떠서 이유 모르겠어서 풀이 좀 봤음
# 투포인터를 쓸 줄 생각도 못했음
# 갈 길이 멀다

import sys
a = int(input())

list1 = list(map(int,sys.stdin.readline().split()))
b = int(input())
list1.sort()

count = 0
start = 0
end = len(list1)-1

while start<end:
    val = list1[start] + list1[end]

    if val > b and end>start:
        end = end-1

    else:
        if val == b:
            count+=1
        start +=1
        end = len(list1)-1

print(count)