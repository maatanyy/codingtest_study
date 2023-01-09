def solution(s):
    answer = []
    for i in range(len(s)):
        count=-1
        for j in range(len(s)):
            if i >j and s[i]==s[j]:
                if count ==-1:
                    count=i-j
                elif count >i-j:
                    count = i-j
        answer.append(count)
