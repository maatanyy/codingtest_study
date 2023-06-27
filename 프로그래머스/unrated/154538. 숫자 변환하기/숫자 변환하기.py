INF = int(1e9)
def solution(x, y, n):
    answer = 0

    d = [INF] * (y+1+n)
    d[x] = 0

    for i in range(x, y+1):

        if i+n<=y:
            d[i+n] = min(d[i+n], d[i]+1)

        if i*2<=y:
            d[i*2] = min(d[i*2], d[i]+1)

        if i*3<=y:
            d[i*3] = min(d[i*3],d[i]+1)

    if d[y]==INF:
        answer = -1
    else:
        answer = d[y]

    return answer

x = 10
y = 40
n = 5

print(solution(x, y, n))


