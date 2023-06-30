import sys

num = int(input())
stack = []

for _ in range(num):
    inputs = sys.stdin.readline().split()

    if inputs[0] == 'push':
        stack.append(inputs[1])

    elif inputs[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()

    elif inputs[0] == 'size':
        print(len(stack))

    elif inputs[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif inputs[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

