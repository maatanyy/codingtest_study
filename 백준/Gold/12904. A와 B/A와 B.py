word1 = str(input())
word2 = str(input())

length1 = len(word1)
length2 = len(word2)

check = False

while word1!=word2:
    if len(word2)==0:
        print('0')
        exit()
    
    if word2[-1]=='A':
        word2 = word2[:-1]
        
    elif word2[-1]=='B':
        word2 = word2[:-1]
        word2 = word2[::-1]
    
    else:
        print('0')
        exit()
    
print('1')