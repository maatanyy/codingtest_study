def solution(str1, str2):
    answer = 2
    for i in range(len(str1)):
        if str1[i:i+len(str2)]==str2:
            answer=1
            break
    return answer
