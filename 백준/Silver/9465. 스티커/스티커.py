testcase = int(input())

for _ in range(testcase):
    a = int(input())
    temp = []

    dp = [[0] *(a) for _ in range(2)]

    for _ in range(2):
        temp.append(list(map(int,input().split())))

    
    
    dp[0][0] = temp[0][0]
    dp[1][0] = temp[1][0]

    if a==1:
        print(max(dp[0][0], dp[1][0]))
        continue
    

    dp[0][1] = dp[1][0] + temp[0][1]
    dp[1][1] = dp[0][0] + temp[1][1]


    if a==2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for i in range(2,a):
        dp[0][i] = max(dp[1][i-2]+temp[0][i],dp[1][i-1]+temp[0][i])
        dp[1][i] = max(dp[0][i-2]+temp[1][i],dp[0][i-1]+temp[1][i])
    
    print(max(dp[0][a-1],dp[1][a-1]))