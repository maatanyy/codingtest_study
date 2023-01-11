n = int(input())
array = list(map(int,input().split()))
array.sort()
m = int(input())
array2 = list(map(int,input().split()))

def search(array,target,start,end):
    if start>end:
        return None

    middle = (start+end)//2

    if array[middle]==target:
        return middle

    elif array[middle]<target:
        return search(array,target,middle+1,end)

    else:
        return search(array,target,start,middle-1)

for i in range(m):
    result = search(array,array2[i],0,n-1)
    if result ==None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

