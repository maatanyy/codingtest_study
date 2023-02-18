num = int(input())
ans = str(input())

ansA = 0
ansB = 0

for i in ans:
    if i=='A':
        ansA+=1
    elif i=='B':
        ansB+=1

if ansA>ansB:
    print('A')
if ansA<ansB:
    print('B')
if ansA==ansB:
    print('Tie')
