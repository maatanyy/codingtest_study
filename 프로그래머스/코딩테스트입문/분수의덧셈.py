# 분수의 덧셈
# 처음에는 케이스를 3개로 나눠서 (분모,분자의 배수기준)으로 접근하여 마지막에 공약수로 나누는 식으로 하였는데
# 이유는 모르겠는데 런타임 오류가 나왔다 아마 수가 커지면 공약수를 구하는데서 오래 걸려서 그런 거 같다
# 그래서 파이썬 공약수 검색해보다 math 라이브러리안에 최대공약수 gcd 구하는게 있는걸 발견해서 이걸 사용해서 해결!
import math

def solution(denum1, num1, denum2, num2):
    answer = []

    num3 = num1 * num2
    denum3 = num1 * denum2 + num2 * denum1

    gcdVal = math.gcd(num3, denum3)

    num3 = num3 // gcdVal
    denum3 = denum3 // gcdVal

    answer.append(denum3)
    answer.append(num3)

    return answer