n, m = map(int, input().split())

values = list(map(int, input().split()))

count = [0] * (m+1)

for i in values:
    count[i]+=1

result = 0

#print(count)
for i in range(len(count)-1):
    first = count[i]
    second = sum(count[i+1:])
    result += (first*second)

print(result)

