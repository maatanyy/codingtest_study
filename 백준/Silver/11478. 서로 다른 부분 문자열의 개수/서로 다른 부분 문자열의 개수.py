words = str(input())

maxlen= len(words)

temp = []

for i in range(maxlen):
    
    start = i
    end = i
    
    while end<=maxlen:

        temp.append(words[start:end])
        end+=1
            

temp = set(temp)

print(len(temp)-1)