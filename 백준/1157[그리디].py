#   x= x.upper() 로 다시 받아줘야하고
# 이 문제에서 배운점은 딕셔너리에 관한 내용
# 딕셔너리를 모르지는 않으나 아직 조금 미숙하다고 느꼈다 특히 키 벨류를 뽑아서 list로 감싼후 count쓰는 건 매우 좋은 방법인 것 같고
# 마지막에 포문 써서 찾은게 살짝 아쉽다
# 인덱스를 사용해도 될 듯 !  temp = arr.index(max) 떄리고 이거 다시 사용해도 될듯

x = str(input())
x= x.upper()
arr = {}

for i in x:
    if i not in arr:
        arr[i] = 1
    if i in arr:
        arr[i] += 1

k = list(arr.keys())     # list로 감쌈
v = list(arr.values())   # list로 감쌈

temp = max(k)   # 큰 키
temp2 = max(v)  # 큰 값

temp3 = v.count(temp2)   # 최대값 수 찾기

if temp3 == 1:
    for k, v in arr.items():
        if v == temp2:
            print(k.upper())
else:
    print('?')


