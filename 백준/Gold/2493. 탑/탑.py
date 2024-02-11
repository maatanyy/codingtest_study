#################
# 나이 풀이 시간초과, 필요없는 애를 스택에서 없애야함
#################
# from collections import deque
# import copy
# import sys

# num = int(input())

# stack= list(map(int,sys.stdin.readline().split()))

# tempstack = copy.deepcopy(stack)

# start = 0
# end = 0
# deque = deque()
# length = len(stack)


# for i in range(num):

#     if len(stack)==0:
#         deque.appendleft('0')
#         break

#     temp = num-i-1
#     start = stack.pop()

#     check =False
#     for i in range(temp,-1,-1):
#         if tempstack[i] > start:
#             deque.appendleft(i+1)
#             check=True
#             break
    
#     if check==False:
#         deque.appendleft(0)

# for i in deque:
#     print(i,end=' ')
            
import sys
input = sys.stdin.readline
n = int(input())
tops = list(map(int,input().split()))
answer= [0] * n
stack = []

for i in range(len(tops)):
    
    while stack:

        if stack[-1][1] > tops[i]:
            answer[i] = stack[-1][0]+1
            break
        
        else:
            stack.pop()
    
    stack.append([i,tops[i]])

print(*answer)