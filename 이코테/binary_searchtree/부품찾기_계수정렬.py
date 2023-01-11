## 답지를 보고 알게 된 풀이ㅣ
## 리스트를 만들고 값들어오면 1로 만들어주고 1 찾는 방식
## 정확히 표현하면 계수 정렬을 사용한 방식임!!
n = int(input())
array = [0]*1000001

for i in input().split():
    array[int(i)] = 1

m= int(input())

x = list(map(int,input().split()))

for i in x:
    if i in array:
        print('yes', end='')
    else:
        print('no', end='')
