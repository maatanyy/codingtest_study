# 잘했다. 하고나서 예제는 돌아가서 맞춘줄 알았는데 틀렸다
# 하지만 접근방식은 일치했는데 여기서 배운점은 반복문에서 이제 보통 그 다음것과 비교하면 range 벗어나는데 범위를 하나 줄인다는 것!
# 이렇게 해도 마지막 까지 비교가 된다!
n = input()

countZero= 0
countOne = 0

if n[0] == 0:
    countZero += 1
elif n[1] == 1:
    countOne += 1

for i in range(len(n)-1):
    if n[i] !=n[i+1]:

        if n[i+1]=='1':
            countZero+=1
        else:
            countOne+=1

print(min(countZero,countOne))