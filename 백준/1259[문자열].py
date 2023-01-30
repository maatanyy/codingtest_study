import sys
arr = []

num = str(input())

if int(num)==0:
    sys.exit(0)

arr.append(num)
while int(num)!=0:
    num = str(input())
    if int(num)!=0:
        arr.append(num)

for i in arr:
    if str(i[:]) == str(i[::-1]):
        print('yes')
    else:
        print('no')
