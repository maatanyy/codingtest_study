# 아이디어는 기깔 났는데 str, int 바꾸는 부분에서 에러가 너무 많이남
# ide에서 오류 말해주니 풀었지 프로그래머스 같은 곳에서 풀었으면 틀렸을 것 같다
n = int(input())

count = 1

while count<=n:

    num = count

    for i in range(len(str(count))):
        count = str(count)
        num += int(count[i])

    if num == n:
        print(count)
        break

    count = int(count)
    count+=1

if count == n+1:
    print(0)






