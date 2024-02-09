import sys

n, s = map(int,input().split())

ans = n+1

temp = list(map(int,sys.stdin.readline().split()))

first = 0
end = 1
value = sum(temp[first:end])

while True:

    if first < 0 or end > len(temp):
        break

    if value >= s:
        ans = min(ans,end-first)
        value = value - temp[first]
        first+=1
        
    elif value<s:
        if end>=len(temp):
            break
        value = value +temp[end]
        end+=1
        

if ans == n+1:
    print('0')
else:
    print(ans)

    
    
    