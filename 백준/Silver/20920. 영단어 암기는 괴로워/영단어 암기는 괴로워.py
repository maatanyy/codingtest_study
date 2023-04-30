import sys

n, m = map(int, sys.stdin.readline().split())

dictionary = {}

for _ in range(n):
    word = str(input())

    if len(word) >= m:
        if word not in dictionary:
            dictionary[word] = [len(word), 1]

        else:
            count = dictionary[word][1]
            dictionary[word] = [len(word), count+1]

result = list(dictionary.items())
result.sort(key=lambda x:(-x[1][1], -x[1][0],x[0]))


for i in result:
    print(i[0])


