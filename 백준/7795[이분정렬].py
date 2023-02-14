# 처음엔 시간 초과
# 어케 할지 고민하다 정렬추가후 중간에 나오게함
# 근데 이것도 돌아가다 시간초과 뜸
# 찾아보니 bisect
# 책에서 읽어보고 실제로는 처음 본건데 개꿀인듯
# 연습할 필요 느꼈음
import bisect
num = int(input())

for _ in range(num):
    n, m = map(int,input().split())

    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))

    count = 0
    arr.sort()
    brr.sort()

    for i in arr:
        count+=bisect.bisect_left(brr,i)

    print(count)