inputs = input()

ans = []

stack = []
check = False

for i in inputs:
    
    if i =='<':
        check = True
        while stack:
            ans.append(stack.pop())
        
    if check==True:
        ans.append(i)
        
    if i=='>':
        check = False
        continue
        
    if check==False:
        if i.isalnum():
            stack.append(i)
        
        else:
            while stack:
                ans.append(stack.pop())
            ans.append(' ')

while stack:
    ans.append(stack.pop())
        
text = ''

for i in ans:
    text +=i
    
print(text)
        
        
        
            
            
    
