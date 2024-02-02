import sys

n, k = map(int, input().split())
temp = list(map(int,sys.stdin.readline().split()))

value = sum(temp[:k])
result = [value]

for i in range(0,len(temp)-k):

    value = value - temp[i] + temp[i+k]
    result.append(value)


print(max(result))