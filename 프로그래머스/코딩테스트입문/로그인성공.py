import sys


def solution(id_pw, db):
    count = 0
    answer = ''
    for data in db:
        if data[0] == id_pw[0] and data[1] == id_pw[1]:
            answer += 'login'
            return answer
        elif data[0] == id_pw[0] and data[1] != id_pw[1]:
            count = 1

    if count == 1:
        answer += 'wrong pw'
    elif count == 0:
        answer += 'fail'

    return answer