# 처음에 대각선  ㅅ 형태를 생각 못했음
# 그 다음은 이제 어떻게 최소를 할까 고민했는데 나는 한 좌표가 0 일경우 직선을 고려했는데
# x,y 최소와 최대 중 하나를 먼저 다 간 상태로 나머지 골하는 방식을 생각을 못했음
# https://stopthebackspace.tistory.com/m/18 참고했음
import sys

x, y, cost1, cost2 = map(int, sys.stdin.readline().split())
# x, y, 걸어서, 대각선

if cost1 * 2 <=cost2:
    answer = x*cost1 + y*cost1

else:
    temp = min(x,y)
    temp2 = max(x,y)
    temp3 = temp2-temp

    answer = temp * cost2

    if cost1>cost2:
        if temp3%2==0:
            answer+=temp3*cost2

        else:
            answer+=(temp3-1)*cost2+cost1

    else:
        answer+=temp3*cost1

print(answer)

