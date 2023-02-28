import sys
n = int(sys.stdin.readline())
answer = 0
list = []

for _ in range(n):
    list.append(int(sys.stdin.readline()))

list.sort(reverse=True)

for i in range(2,len(list),3):
    answer+=list[i]

print(sum(list)-answer)
