num = int(input())

dict = {}
temp = []

for i in range(num):
    temp.append(input())


for word in temp:

    square = len(word) - 1
    for c in word:
        if c in dict:
            dict[c] += pow(10, square)
        else:
            dict[c] = pow(10, square)
        square -= 1

dict = sorted(dict.values(), reverse=True)


result = 0
first = 9
for i in dict:
    result+= i*first
    first-=1

print(result)

