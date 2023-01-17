# 반복문 써서 뭐 자리수별로 숫자 만들어서 확인해서 30의 배수면 변수에 담아뒀다가 제일 큰거 나올 때 까지 하는식인줄 알았음
# 걍 붕신이었다
# 배수 문제를 많이 안접해봐서 그런 거 같은데 기본적으로 n의 배수 문제가 나오면 그 배수가 되는 공식을 알고 그것에 의존해서 설계하는 게 방법인듯
n = list(map(str, input()))
n.sort(reverse=True)

if '0' not in n:
    print(-1)

else:
    Num = int(''.join(n))
    if Num % 30 == 0:
        print(Num)
    else:
        print(-1)
