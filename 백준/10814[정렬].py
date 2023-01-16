# 입력이 많을 때 sys 쓰기 기억해두자
# 그리고 이제 중요한게 여기서 int로 나이를 감싸야함 아니면 11, 9일경우 1만 인식해서 먼저 오는 예외발생!! 이걸 몰라서 틀렸다가 헤맴
import sys

n = int(sys.stdin.readline())

array = []

for i in range(n):
    age, name = sys.stdin.readline().split()

    userinfo = (int(age),name)
    array.append(userinfo)


array.sort(key=lambda x: x[0])

for i in array:
    print(i[0],i[1])