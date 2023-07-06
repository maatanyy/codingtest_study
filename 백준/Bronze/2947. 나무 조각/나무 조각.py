temp = list(map(int,input().split()))


def print_arr(array):
    for i in array:
        print(i,end=' ')
    print()

for i in range(len(temp)-1):
    for j in range(0,len(temp)-i-1):
        if temp[j]>temp[j+1]:
            temp[j],temp[j+1] = temp[j+1], temp[j]
            print_arr(temp)
