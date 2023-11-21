# 준하는 블로그를 운영하고 있습니다.
# 용돈을 벌고 싶었던 준하는 블로그에 광고를 달려고 합니다.
#
# 광고를 달기 위해서는 블로그의 방문자 수가 많을 수록 유리합니다.
# 블로그의 관리자 메뉴에는 N일간의 방문자의 수가 기록되어 있는데,
# 준하는 이 기록중 연속된 K일만 빼고 모두 삭제해서 평균 방문자가 더 많은 것처럼 만드려고 합니다.
# 가장 많은 평균 방문자가 표시되도록 하기 위해서는 몇 번째 날 부터 K일만 남겨야 하는지 계산하는 프로그램을 작성해 주세요.
n, m = map(int, input().split())
vals = list(map(int, input().split()))

temps = []

for i in range(n-m+1):
    k = sum(vals[i:i+m])/m
    temps.append(k)

print(temps.index(max(temps))+1)