# 나의 풀이

x, y = map(int, input().split())

result = 0
for i in range(x):
    data = list(map(int, input().split()))
    minValue = min(data)

    result = max(result,minValue)

print(result)

# 책의 2중 반복문 구조를 이용한 답안

# result=0
# for i in range(x):
#     data = list(map(int, input().split()))
#     min_value=10001
#     for a in data:
#         min_value= min(min_value,a)
#     result = max(result,min_value)
# print(result)