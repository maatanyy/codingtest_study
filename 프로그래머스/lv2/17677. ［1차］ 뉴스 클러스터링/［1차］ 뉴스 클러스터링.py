def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    valid ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #print(str1)
    #print(str2)
    length1 = len(str1)
    length2 = len(str2)

    temp1 = []
    temp2 = []
    temp3 = []

    for i in range(length1-1):
        val = str1[i:i+2]
        if val[0] in valid and val[1] in valid:
            temp1.append(val)

    for j in range(length2-1):
        val = str2[j:j+2]
        if val[0] in valid and val[1] in valid:
            temp2.append(val)

    temp1.sort()
    temp2.sort()

    len1 = len(temp1)
    len2 = len(temp2)

    if len1 ==0 and len2==0:
        return 65536

    count = 0
    for i in range(len1):
        for j in range(len2):
            if temp1[i]==temp2[j]:
                count+=1
                temp3.append(temp1[i])
                temp1[i] = '*'
                temp2[j] = '*'


    for i in temp1:
        if i !='*':
            temp3.append(i)

    for j in temp2:
        if j !='*':
            temp3.append(j)


    tempLength = len(temp3)

    answer = int(count/tempLength *65536)

    return answer

str1 = 'E=M*C^2'
str2 = 'e=m*c^2'

print(solution(str1,str2))


