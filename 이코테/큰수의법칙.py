#input 입력 받기 map , list를 사용
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

# sort 한 후 first 와 second를 구해줌 결국 first 와 second만 쓰임
data.sort()

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):  #k만큼 최대수를 더 해줌
        if m==0:
            break
        result += first
        m-=1
    if m==0:
        break
    result +=second    #k만큼 최대수를 더한 후 두번째 수 한번 더해주는 과정
    m-=1
print(result)

