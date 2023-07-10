n, m = map(int, input().split())

temp = list(map(int, input().split()))

count = 0
totalval = 0
end = 0

for start in range(n):

    while totalval<m and end<n:
        totalval+=temp[end]
        end+=1

    if totalval ==m:
        count+=1

    totalval -=temp[start]

print(count)