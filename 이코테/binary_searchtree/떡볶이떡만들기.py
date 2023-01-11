# 잘 풀었다
# 다만 고민했던 부분이 result를 어디서 뽑아내냐였다
n, m = map(int,input().split())
array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0

while start<=end:

    middle = (start+end)//2

    total = 0

    for x in array:
        if x > middle:
            total += x-middle

    if total < m:
        end = middle-1

    else:
        result = middle
        start = middle+1

print(result)
