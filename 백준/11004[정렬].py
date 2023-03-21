import sys

n, m = map(int, input().split())

temp = list(map(int,sys.stdin.readline().split()))

temp.sort()
print(temp[m-1])