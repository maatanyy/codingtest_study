# 이진탐색을이용하여 앞에 있으면 이동하는시ㅣㄱ으로 처음을 찾았고
# 그 이후에는 반복문을 통해서 마지막을 찾았는데 주석 달면서 생각해보니 이러면 O(N)이라 안될 것 같다 ㅋ
x, y = map(int, input().split())
array = list(map(int, input().split()))

def search(array, target, start, end):
    while start <= end:
        middle = (start+end)//2

        if array[middle] == target:
            if array[middle-1] == target:
                end = middle - 1
            else:
                return middle

        elif array[middle] < target:
            start = middle+1
        else:
            end = middle-1
    return None

result = search(array, y, 0, x-1)

if result == None:
    print('-1')

else:
    count = 0
    for i in range(result, x):
        if array[i] == y:
            count += 1
        else:
            break
    print(count)


