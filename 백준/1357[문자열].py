val1, val2 = list(map(str,input().split()))

temp=''
temp2=''

for i in val1:
    temp= i+temp

for i in val2:
    temp2=i+temp2

temp = int(temp)
temp2 = int(temp2)
temp3 = int(temp+temp2)
temp3 = str(temp3)

ans = ''

for i in temp3:
    ans = i+ans

print(int(ans))