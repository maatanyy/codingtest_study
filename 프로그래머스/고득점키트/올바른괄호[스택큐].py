def solution(s):
    a = []
    for i in range(len(s)):
        if s[i]=='(':
            a.append(s[i])

        else:
            if len(a) == 0:
                return False
            else:
                a.pop()
    if len(a)!=0:
        return False
    else:
        return True


################# 다른 풀이 , 예외처리를 씀
#
# def is_pair(s):
#     st = list()
#     for c in s:
#         if c == '(':
#             st.append(c)
#
#         if c == ')':
#             try:
#                 st.pop()
#             except IndexError:
#                 return False
#
#     return len(st) == 0