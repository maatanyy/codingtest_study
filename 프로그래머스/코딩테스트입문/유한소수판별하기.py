# gdc 는 생각을 했는데
# while 2번으로 해결하는 방식을 생각을 못했다..

from math import gcd

def solution(a, b):
    temp = b // (gcd(a, b))

    while temp%2==0:
        temp=temp//2
    while temp%5==0:
        temp=temp//5

    if temp==1:
        answer=1
    else:
        answer =2
    return answer
