# 아이디어가 안떠올라서 노가다로 했는데 역시나 시간초과 및 틀림...
# 홀수 짝수로 접근하는 방법을 생각해보면 괜찮을 것 같다는 생각이 들고 확실히 머리를 써야하는 것 같다
n = int(input())
m = int(input())
lights = list(map(int, input().split()))


if len(lights) == 1:
    height = max(lights[0],n-lights[0])

else:
    height = lights[0]

    for i in range(len(lights)):
        if i== (len(lights)-1):
            temp = n-lights[-1]
        else:
            value = lights[i+1]-lights[i]

            if value%2==0:
                temp = value//2
            elif value%2==1:
                temp = value//2 +1

        height = max(height,temp)

print(height)






