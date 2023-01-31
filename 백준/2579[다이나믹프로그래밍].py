num = int(input())
arr = [0]* (num)
drr = [0]* (num)

for i in range(num):
    arr[i] = int(input())

if len(arr)<2:
    print(sum(arr))

else:
    drr[0] = arr[0]
    drr[1] = arr[0]+arr[1]
    for i in range(2,num):
        drr[i]= max(drr[i-3]+arr[i-1]+arr[i],drr[i-2]+arr[i])
    print(drr[-1])