num = int(input())

list = []
for _ in range(num):

    temp = int(input())

    if temp==0:
        list.pop()

    else:
        list.append(temp)

print(sum(list))