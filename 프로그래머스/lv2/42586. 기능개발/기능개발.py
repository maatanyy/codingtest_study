def solution(progresses, speeds):
    temps = []
    answer = []
    for i in range(len(progresses)):
        for j in range(1, 100):
            if progresses[i] + (speeds[i] * j) >= 100:
                temps.append(j)
                break

    now = 0
    n = len(progresses)
    for i in range(1,n):
        if temps[now]<temps[i]:
            answer.append(i-now)
            now = i
    answer.append(n-now)
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))

# [1, 3, 2]














