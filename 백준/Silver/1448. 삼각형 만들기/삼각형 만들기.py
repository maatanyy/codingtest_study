from itertools import combinations
import sys

num = int(input())

temp = []

for _ in range(num):
    temp.append(int(sys.stdin.readline()))


temp.sort(reverse=True)

for i in range(num-2):
    if temp[i] < temp[i+1] + temp[i+2]:
        print(temp[i] + temp[i+1] + temp[i+2])
        quit()

print(-1)