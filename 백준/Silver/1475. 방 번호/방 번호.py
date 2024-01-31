from collections import Counter
import sys
import math

value = str(input())

value = value.replace('6','9')

counter = Counter(value)

temp = counter.most_common(2)

ans = -1


for k,v in temp:

    if k =='9':
        ans = max(ans,math.ceil(v/2))
    
    else:
        ans = max(ans,v)


print(ans)

