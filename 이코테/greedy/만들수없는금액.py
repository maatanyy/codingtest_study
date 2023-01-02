# 정렬까지 생각은 좋았음
# for문 을 생각못했다..
# 정렬 생각한걸로 일단 만족
n = input().split()

data = list(map(int, input().split()))
data.sort()
start = 1

for i in data:
    if start < i:
        break
    start += i

print(start)
