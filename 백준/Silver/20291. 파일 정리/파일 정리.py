num = int(input())

dict = {}
for _ in range(num):
    inputs = list(map(str,input().split('.')))
    
    if inputs[1] not in dict:
        dict[inputs[1]] =1
    
    else:
        dict[inputs[1]]+=1
        

items_list = list(dict.items())
    
items_list.sort(key=lambda x:x[0])

for i in items_list:
    print(i[0], i[1])
