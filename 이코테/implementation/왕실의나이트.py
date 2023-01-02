# char을 int로 바꾸는 것을 ord()를 사용한다는 것을 검색을 통해 알아내었고 이를 통해 문제를 해결할 수 있었다.
# moveX, moveY로 넣어두는 패턴은 어느정도 감을 잡은 것 같다
n = input()
X = ord(n[0])-96
Y = int(n[1])
count = 0

moveX = [1,2,2,1,-1,-2,-2,-1]
moveY = [-2,-1,1,2,2,1,-1,-2]

for i in range(len(moveX)):
    changeX = X+moveX[i]
    changeY = Y+moveY[i]

    if changeX >=1 and changeX <=8 and changeY >=1 and changeY <=8:
        count+=1

print(count)
