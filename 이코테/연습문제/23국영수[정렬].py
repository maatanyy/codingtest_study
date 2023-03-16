import sys

num = int(sys.stdin.readline())
list= []

for _ in range(num):
    list.append(sys.stdin.readline().split())

list.sort(key = lambda x: (-int(x[1]), int(x[2]),-int(x[3]), x[0]))

for i in list:
    print(i[0])

