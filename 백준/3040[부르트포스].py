from itertools import combinations
arr = []

for _ in range(9):
    num = int(input())
    arr.append(num)

temp = list(combinations(arr,7))

for i in temp:
    ans = 0
    for j in i:
        ans+=j

    if ans == 100:
        temp2 = i
        break

for i in temp2:
    print(i)