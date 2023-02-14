import sys
n, m = map(int,input().split())

package = 1000
one = 1000

for i in range(m):
    x, y = map(int,input().split())
    if x<package:   # 낱개
        package=x
    if y<one:   # 패키지
        one=y


if package >= 6*one:
    print(n*one)

else:
    sum = package*(n//6)
    rest = n%6
    if package > one * rest:
        sum+=one*rest
    else:
        sum+= package

    print(sum)






