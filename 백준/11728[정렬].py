import sys
a, b = map(int,input().split())

list1 = list(map(int,sys.stdin.readline().split()))
list2 = list(map(int,sys.stdin.readline().split()))

list3 = list1+list2
list3.sort()

for i in list3:
    print(i,end=' ')