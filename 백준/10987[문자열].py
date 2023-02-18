val = str(input())

count = 0

for v in ('a','e','i','o','u'):
    count+=val.count(v)
print(count)