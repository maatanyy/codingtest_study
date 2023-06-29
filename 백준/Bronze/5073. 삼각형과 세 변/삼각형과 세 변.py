while True:
    x, y, z = map(int,input().split())
    temp = []
    temp.append(x)
    temp.append(y)
    temp.append(z)

    if x == 0 and y == 0 and z == 0:
        break

    else:
        maxVal = max(temp)
        temp.remove(maxVal)
        secondVal = max(temp)
        temp.remove(secondVal)
        thirdVal = temp[0]

        if maxVal >= secondVal+thirdVal:
            print("Invalid")

        elif x==y and y==z:
            print("Equilateral")

        elif x==y!=z or x==z!=y or y==z!=x:
            print("Isosceles")

        elif x!=y!=z:
            print("Scalene")

