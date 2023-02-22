# 너무 복잡하게 생각함
# 문제 이해를 잘 못했다
# sort 까지는 생각하고 그 이후 고민인데
# 중간에 if 문 부분을 생각을 못함

def solution(citations):
    citations.sort()
    article_count = len(citations)

    print(citations)
    for i in range(article_count):
        if citations[i] >= article_count-i:
            return article_count-i
    return 0

print(solution([3, 0, 6, 1, 5]))