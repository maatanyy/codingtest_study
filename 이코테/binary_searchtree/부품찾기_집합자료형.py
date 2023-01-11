## 답지를 보고 알게 된 풀이ㅣ
## 단순히 특정한 수가 한 번이라도 등장했는지를 검사하면 되므로 집합 자료형을 이용함
## 단순히 한 번이라도 등장 -> 집합 자료형 생각하자!!

n = int(input())

array = set(map(int,input().split()))

m = int(input())

x = list(map(int,input().split()))

for i in x:

    if i in array:
        print('yes', end='')
    else:
        print('no', end= '')
