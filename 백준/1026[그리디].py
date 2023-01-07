#쉽게 해결 remove 아이디어 좋았다

n = input()

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum =0

for x in range(len(a)):
    sum += min(a)*max(b)
    a.remove(min(a))
    b.remove(max(b))

print(sum)
