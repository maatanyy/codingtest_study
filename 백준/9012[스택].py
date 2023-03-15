import sys
n = int(sys.stdin.readline())

for i in range(n):
    temp = list(map(str,input()))

    ans = []
    check = 0
    for i in temp:
        if i == '(':
            ans.append('(')
        else:
            if len(ans)!= 0:
                ans.pop()
            else:
                check = 1
                break

    if check == 1 or len(ans)!=0:
        print('NO')
    else:
        print('YES')