#page 321 구현. 쉽게 해결!
#풀고 풀이를 보니 answer를 2개로 구분하여 비교하지 말고 다 더하고 반대로 다 빼서 0이랑 비교하는 방법을 사용한게 인상 깊었다.
n = str(input())
divide = int(len(n)/2)

answer=0
answer2=0

for i in range(divide):
    answer+=int(n[i])

for i in range(divide,int(len(n))):
    answer2+=int(n[i])

if answer == answer2:
    print('LUCKY')
else:
    print('READY')
