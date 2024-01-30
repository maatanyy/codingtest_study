num = int(input())

temp = []

for _ in range(num):
    temp.append(int(input()))

temp.sort()

answers = []

for x in temp:
    answers.append(x*num)
    num -= 1
print(max(answers))