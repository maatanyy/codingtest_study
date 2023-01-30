T = int(input())
moneys = [25, 10, 5, 1]
count = [0] * 4

for i in range(T):
    C = int(input())

    for j in range(len(moneys)):
        count[j] = C // moneys[j]
        C = C % moneys[j]
    ## 요부분 출력하는 부분을 기억하자!!
    # ''.join()형태는 알고 있었지만 map(str,count)같은 형식은 또 처음 이런것도 있구나 싶었다
    print(' '.join(map(str, count)))

