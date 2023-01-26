### in list O(n), in set O(1)이라는 걸 알게 되었다!!!
num = int(input())
array = list(map(int,input().split()))
num2 = int(input())
array2 = list(map(int,input().split()))

array = set(array)
for i in range(num2):
    if array2[i] in array:
        print('1')
    else:
        print('0')


