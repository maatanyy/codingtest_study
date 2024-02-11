num = int(input())

infos = [list(map(int,input().split())) for i in range(num)]


dp = [0 for i in range(num+1)]


for i in range(num):

    for j in range(i+infos[i][0],num+1):

        if dp[j] < dp[i]+infos[i][1]:
            dp[j] = dp[i]+infos[i][1]

print(dp[-1])