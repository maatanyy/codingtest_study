n, m = map(str, input().split())

if len(n) == len(m):
    count = 0
    for i in range(len(n)):
        if n[i] != m[i]:
            count+=1
    print(count)

else:
    count = 51
    diff = len(m) - len(n)

    for i in range(diff+1):
        count2 = 0
        tempstr = m[i:i+len(n)]
        #print(tempstr)
        for j in range(len(n)):
            if n[j] != tempstr[j]:
                count2+=1

        count = min(count,count2)
    print(count)