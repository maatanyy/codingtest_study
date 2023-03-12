from collections import deque
n, m = map(int, input().split())

li = deque()
for i in range(n):
    li.append(i+1)

print('<', end = '')
while li:
    for i in range(m-1):
        li.append(li[0])
        li.popleft()

    if len(li) != 1:
        print(li[0], end=', ')
        li.popleft()
    else:
        print(li[0], end='')
        li.popleft()

print('>')

