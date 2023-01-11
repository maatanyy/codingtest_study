def binary_searchtree(array, target, start, end):
    if start > end:
        return None

    middle = (start +end) //2  # 몫만 구하기 위해서 //를 사용

    if array[middle] == target:
        return middle

    elif array[middle] > target:
        return binary_searchtree(array, target, start, middle-1)

    else:
        return binary_searchtree(array, target, middle+1, end)

n, target = list(map(int,input().split()))   # n은 array수
array = list(map(int,input().split()))

result = binary_searchtree(array, target,0,n-1)

if result == None:
    print("존재하지않습니다")
else:
    print(result+1)





