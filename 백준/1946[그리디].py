# 처음에 짠 코드는 잘 동작했는데 시간초과가 났다
# for문을 2번 써서 n제곱 시간 복잡도를 가져서 그렇다고 한다
# 그래서 for문을 하나만 써야하는데 이제 이걸 살짝 도움 받았다
# sort 쓴 후 if로 비교해가며 하는 건데  이제 다른 애들보다 무조건 낮으면 안된다는 성질을 이용한다
# 무조건 작으면 안된다라는 성질 떄문에 다 보지 않고 쭉 원사이드로 넘어가며 if로 비교할 수 있따는 것응 알게 되었다
# x = int(input())
# ans = []
#
# for i in range(x):
#     array = []
#     num = int(input())
#
#     for _ in range(num):
#         a, b = input().split()
#         array.append((a,b))
#
#     array.sort(reverse=True)
#
#     count2 = 0
#     for i in range(num):
#         count = 0
#         for j in range(i+1,num):
#             if array[i][0] > array[j][0] and array[i][1] > array[j][1]:
#                 count+=1
#                 break
#
#         if count==1:
#             count2+=1
#
#     ans.append(num-count2)
#
# for i in ans:
#     print(i)

import sys
x = int(sys.stdin.readline())
ans = []

for i in range(x):
    array = []
    num = int(sys.stdin.readline())
    count = 1

    for _ in range(num):
        a, b = map(int,sys.stdin.readline().split())
        array.append([a,b])

    array.sort()
    val = array[0][1]

    for i in range(1, num):
        if val > array[i][1]:
            count+=1
            val = array[i][1]

    ans.append(count)

for i in ans:
    print(i)
