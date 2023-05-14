import sys

text = str(input())

count1 = 0
count2 = 0
for i in text:
    if i=='1':
        count1+=1
    else:
        count2+=1

temp = '1' * int(count1/2)
temp2 = '0' * int(count2/2)

temp = temp2+temp

print(temp)
