num = int(input())

temp = [-1] * (num)
numbers = list(map(int,input().split()))

stack = []

for idx, number in enumerate(numbers):

    while stack and numbers[stack[-1]]<number:
        temp[stack.pop()] = number

    stack.append(idx)

for i in temp:
    print(i,end=' ')