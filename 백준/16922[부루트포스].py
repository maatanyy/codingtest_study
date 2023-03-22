from itertools import combinations_with_replacement

temp = [1,5,10,50]

num = int(input())

product_ans = list(combinations_with_replacement(temp, num))
temp_ans = []

count = 0
for i in product_ans:
    answer = 0
    for j in range(len(i)):
        answer+=i[j]

    temp_ans.append(answer)

temp_ans = set(temp_ans)

print(len(temp_ans))





