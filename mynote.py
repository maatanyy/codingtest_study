###########################################
#  1. 투포인터
#  2. 정렬되어 있는 두 리스트의 합집합
#  3. 접두사 합을 활용한 구간 합 계산 소스코드
#  4. 에라토스테네스의 체 이용한 소수 구하기

###########################################



#################################
#            투포인터            #
#################################

n = 5    # 길이
m = 5    # 찾으려고 하는 부분합
data = [1,2,3,2,5]

count = 0    # 수
interval_sum = 0   # 부분합
end = 0  # end 포인터 위치

for start in range(n):

    while interval_sum<m and start<n:   # 작으면 end 옮기고 같거나 크면 start 옮긴다
        interval_sum += data[end]
        end+=1

    if interval_sum ==m:                # 찾는 부분합과 같을 경우 count 증가
        count+=1

    interval_sum-=data[start]           # start가 가르키는 값을 빼준다

print(count)


#################################
#   정렬되어 있는 두 리스트의 합집합   #
#################################

n, m = 3, 4
a = [1, 3, 5]
b = [2,4,6,8]

result = [0] * (m+n)
i, j, k = 0, 0, 0

while i<n or j<m:

    if j>=m or (i<n and a[i]<b[j]):
        result[k] = a[i]
        i+=1

    else:
        result[k] = b[j]
        j+=1

    k+=1

print(result)


#########################################
#   접두사 합을 활용한 구간 합 계산 소스코드   #
#########################################

n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value+=i
    prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right]-prefix_sum[left-1])


#########################################
#   에라토스테네스의 체 이용한 소수 구하기    #
#########################################

import math
m, n = map(int, input().split())
array = [True for i in range(1000001)]
array[1] = 0

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j+=1

for i in range(m,n+1):
    if array[i]:
        print(i)








