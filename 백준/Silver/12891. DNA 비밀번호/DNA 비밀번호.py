from collections import deque

start, num = map(int,input().split())

temp = list(str(input()))

A,C,G,T = map(int, input().split())

dic = {'A':0, 'C':0, 'G':0, 'T':0}

left, right = 0, num-1
q = deque(temp[left:right])

for i in q:
    dic[i] +=1

count = 0
    
while right< start:
    
    dic[temp[right]]+=1
    
    if dic['A']>=A and dic['C'] >=C and dic['G']>=G and dic['T'] >=T:
        count+=1
    
    dic[temp[left]]-=1
    left+=1
    right+=1
    
print(count)
        
    