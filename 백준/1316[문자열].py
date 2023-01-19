# 잘 푼 것 같다
# 처음에 공백으로 선언해주고 공백이면 넣어주고
# 인덱스 -1을 통해 마지막과 비교하여 해결!
x = int(input())
arr = []

for _ in range(x):
    arr.append(str(input()))

count = 0

for i in arr:
    temp = ''
    for j in i:
        if temp == '':
            temp+=j
        elif j not in temp or temp[-1]==j:
            temp+=j
        else:
            count+=1
            break

print(x-count)


