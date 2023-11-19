def solution(n, lost, reserve):
    student = [1]*n

    for i in lost:
        student[i-1] = 0 

    for i in reserve:
        student[i-1] += 1

    first_student = student[0]
    last_student = student[len(student)-1]

    if first_student == 0:
        if student[1] == 2:
            student[0] = 1
            student[1] = 1

    if last_student == 0:
        if student[len(student)-2] == 2:
            student[len(student)-1] = 1
            student[len(student)-2] = 1

    for i in range(1, len(student)-1):
        if student[i] == 0:
            if student[i-1] == 2:
                student[i] = 1
                student[i-1] = 1
            elif student[i+1] == 2:
                student[i] = 1
                student[i+1] = 1
    return student.count(1) + student.count(2)
