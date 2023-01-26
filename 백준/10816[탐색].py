### in list O(n), in set O(1)이라는 걸 알게 되었다!!!
num = int(input())
array = list(map(int,input().split()))

num2 = int(input())
array2 = list(map(int, input().split()))

d1 = dict()
for i in array:
    if d1.get(i) == None:
        d1[i] = 1
    else:
        d1[i] += 1

for i in array2:
    if d1.get(i) == None:
        print(end='0 ')
    else:
        print(d1[i], end=' ')