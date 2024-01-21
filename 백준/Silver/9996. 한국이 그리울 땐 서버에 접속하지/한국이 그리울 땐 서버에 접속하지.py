num = int(input())

pattern = input().split('*')

maxlen = len(pattern[0]) +len(pattern[1])

for _ in range(num):
    
    arr = input()
    
    if len(arr)>=maxlen and arr.startswith(pattern[0]) and arr.endswith(pattern[1]):
        print('DA')
    
    else:
        print('NE')