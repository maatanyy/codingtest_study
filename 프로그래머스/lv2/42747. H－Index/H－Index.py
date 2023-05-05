def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    print(citations)
    num = citations[0]
    # 어떤 과학자가 발표한 논문 n편중, h번 이상 인용된 논문이 h편이상이고
    # 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H - Index입니다.

    while True:
        count = 0
        for i in citations:
            if num<=i:
                count+=1


        if count>=num:
            answer = num
            break

        else:
            num = num-1

    return answer