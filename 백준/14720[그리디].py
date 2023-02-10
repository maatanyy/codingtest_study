# 잘푼듯 굳굳 마지막에 else에서 처음에 continue했다가 반복문이 안끝난다는 걸 인지하고 다음으로 넘기는 식으로 해결했다
num = int(input())

arr = list(map(int,input().split()))

count = 0
check = 0
while arr:
    if arr[0]==0 and check==0:
        arr=arr[1:]
        check=1
        count+=1
        print('*')
    elif arr[0]==1 and check==1:
        arr=arr[1:]
        check=2
        count+=1
        print('&')
    elif arr[0]==2 and check==2:
        arr=arr[1:]
        check=0
        count+=1
        print('%')
    else:
        arr=arr[1:]

print(count)