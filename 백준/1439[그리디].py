# 5분컷해야하는데 20분은 쓴듯
# 방법도 알았는데 너무 헤맴 연습이 더 필요한가보다
# 출력부분을 경우 나눠서 했는데 왜 그렇게했나 싶네요
import sys
s = sys.stdin.readline()

Num1 = 0
Num2 = 0

for i in range(len(s) - 1) :
    if s[i] != s[i+1] and s[i] == "0" :
        Num2 += 1
    elif s[i] != s[i+1] and s[i] == "1" :
        Num1 += 1

print(min(Num1, Num2))
