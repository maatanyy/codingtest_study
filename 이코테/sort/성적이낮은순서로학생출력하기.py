# 람다 활용에 집중!
# 한번 쓰고 안쓰는 함수에 사용한다. lambda ~~ : ~
n = int(input())

array=[]

for i in range(n):
    indata = input().split()
    array.append((indata[0], int(indata[1])))

array = sorted(array,key=lambda student:student[1])

for student in array:
    print(student[0],end='')
print(array)