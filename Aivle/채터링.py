
# 채터링이란 스위치의 상태가 변하는 순간, 10ms 이내에 열림과 닫힘이 수 회 반복되는 현상을 말합니다.
# 준하의 키보드에 채터링 현상이 일어나서, 어떤 문자를 한 번 입력하면 K회 반복해서 출력됩니다.
# 준하가 입력하려는 문자열이 주어질 때, 출력되는 문자열을 출력하는 프로그램을 작성해 주세요.


n, m = map(int,input().split())

inputs = input()

ans = ''

for i in range(len(inputs)):
    for j in range(m):
        ans+=inputs[i]

print(ans)