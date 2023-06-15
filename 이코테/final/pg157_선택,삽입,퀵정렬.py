array = [7,5,9,0,3,1,6,2,4,8]

# 선택정렬
for i in range(len(array)):
    minid = i
    for j in range(i+1,len(array)):
        if array[minid]>array[j]:
            minid = j

    array[i],array[minid] = array[minid],array[i]

print(array)

# 삽입정렬
for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break

print(array)

def quick_sort(array):
    if len(array)<=1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x<=pivot]
    right = [x for x in tail if x>pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))




















