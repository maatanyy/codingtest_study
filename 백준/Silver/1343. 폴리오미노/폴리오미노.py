from collections import deque
values = str(input())

values = values.replace('XXXX','AAAA')
values = values.replace('XX','BB')

if values.count('X')!=0:
    print(-1)
else:
    print(values)