## 다시 풀어봐야함
## d[1]에서 max쓰는 것을 생각 못했다,,,
## 아직 낯설지만 마지막부터 거꾸로 생각해보며 규칙찾는 것이 중요한듯!
x = int(input())
array = list(map(int, input().split()))

d = [0]*101

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, x):
    d[i] = max(d[i-2]+array[i], d[i-1])

print(d[x-1])

