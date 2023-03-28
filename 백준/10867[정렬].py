import sys

num = int(input())

temp = list(map(int, sys.stdin.readline().split()))

temp =list(set(temp))

temp.sort()

for i in temp:
    print(i, end=' ')