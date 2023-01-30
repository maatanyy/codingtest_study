text = str(input())

arr = [0]*26

for i in text:
    arr[ord(i)-ord('a')]+=1

for i in arr:
    print(i)