#다른 사람의 풀이를 참고하였는데
# 내가 한 실수는 1. 처음 sort를 쓰지 않아서 for문 2개를 사용했다는 점과
# 2. 이제 중간에 글자가 포함된 것 까지 맞다고 해버렸다 여기서는 이제 인덱싱을 사용해서 해결하는데 이걸 이제 배운 것 같다
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][0:len(phone_book[i])]:
            return False
    return True

print(solution(["119", "97674223", "1195524421"]))