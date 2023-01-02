# 4-2 시각
# n 을 입력받아 for문 3개 쓰는 것 까지는 생각함
# 하지만 str(i)+str(j)+~~~ 를 '3'으로 푸는 법을 생각하지 못했다.
# str()+str() 형태에 대해 알게 됨
n = int(input())

count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1

print(count)
