def solution(number, k):
    answer = ''
    stack = []

    for i in number:

        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        stack.append(i)

    if k>0:
        stack = stack[:-k]


    return ''.join(stack)