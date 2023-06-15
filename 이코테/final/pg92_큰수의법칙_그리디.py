n, m, k = map(int, input().split())

temp = list(map(int, input().split()))

temp.sort(reverse=True)

sumVal = 0

num1 = temp[0]
num2 = temp[1]

while True:
    for i in range(k):
        if m==0:
            break

        sumVal +=num1
        m-=1

    if m==0:
        break
    sumVal += num2
    m-=1

print(sumVal)


