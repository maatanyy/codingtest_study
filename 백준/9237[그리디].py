# reverse = True 까지는 좋았다.
# 여기서 이제 어케 할까 고민하며 나는 다른 배열을 하나 만들어서 옮기는 방식으로 해결하였는데 시간 초과가 뜸...
# 인덱스 합으로 해결하는 방법이 있다니.. 하루마다 하나씩 심으니까 가능한 접근인 것 같다

num = int(input())

arr = list(map(int,input().split()))

arr.sort(reverse=True)

count = 1
result = 0

for i in range(num):
    if arr[i] + count > result:
        result = arr[i]+count
    count+=1

print(result+1)