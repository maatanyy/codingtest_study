homework = dict()

for i in range(30):
    homework[i+1] = 0

for i in range(28):
    x = int(input())
    homework[x] = 1

for i in range(30):
    if homework[i+1] ==0 :
        print(i+1)