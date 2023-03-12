from collections import deque
n = int(input())

li = deque()
for i in range(n):
    li.append(i+1)

while len(li)!=1:
    li.popleft()
    li.append(li[0])
    li.popleft()

print(li[0])


