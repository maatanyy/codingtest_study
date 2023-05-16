from itertools import combinations

n, m = map(int, input().split())

values = list(map(str, input().split()))
values.sort()
moum = 'aeiou'
temp1 = []
temp2 = []

answer = []
for password in combinations(values,n):

    count = 0
    for i in password:
        if i in moum:
            count+=1

    if count>=1 and count<= n-2:
        answer.append(password)


for i in answer:
    print(''.join(i))













