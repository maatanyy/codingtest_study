n = int(input())

array = list(map(int,input().split()))

m = int(input())

array2 = list(map(int,input().split()))

array.sort()

def binary_search(array,target,start,end):

    while start<=end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            start = mid+1

        elif array[mid] > target:
            end = mid-1

    return None

for i in array2:
    result = binary_search(array,i,0,len(array)-1)
    if result==None:
        print('no',end=' ')
    else:
        print('yes',end=' ')











