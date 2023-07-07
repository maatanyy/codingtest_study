def solution(brown, yellow):
    total = brown + yellow
    answer = []
    for i in range(3, total + 1):

        if total % i == 0:
            j = total // i

            graph = [[0 for _ in range(j)] for _ in range(i)]

            count = 0
            for t in range(i):
                for k in range(j):
                    if t!=0 and t!= i-1 and k!=0 and k!=j-1:
                        graph[t][k] = 1
                        count+=1

            if count == yellow:
                answer.append(j)
                answer.append(i)
                break

    return answer

brown = 24
yellow = 24

print(solution(brown, yellow))
    


  