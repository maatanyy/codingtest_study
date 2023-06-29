num = int(input())
one1 = 100
one2 = 100
for _ in range(num):
    a, b = map(int, input().split())

    if a>b:
        one2-=a
    elif a<b:
        one1-=b

print(one1)
print(one2)


