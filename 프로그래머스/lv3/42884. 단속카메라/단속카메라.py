def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    print(routes)
    check = -30001

    for route in routes:
        if check < route[0]:
            answer += 1
            check = route[1]

    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))