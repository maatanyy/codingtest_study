## 중간에 or가 아니라 +로 하는 이유를 생각해봐야할듯
## or로 하면 겹치는게 있어서 더 큰 수가 나오는 것 같다

num = int(input())

count = 0

for i in range(num+1):
    for k in range(60):
        for t in range(60):
            if '3' in str(i) + str(k) + str(t):
                count+=1

print(count)