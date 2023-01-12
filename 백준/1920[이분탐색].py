n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
array2 = list(map(int, input().split()))

def search(array,target,start,end):
    if start > end:
        return None

    middle = (start+end)//2

    if array[middle] == target:
        return middle

    elif array[middle] < target:
        return search(array, target, middle+1, end)

    else:
        return search(array, target, start, middle-1)

for x in array2:
    result = search(array,x,0,n-1)
    if result == None:
        print("0")
    else:
        print("1")
