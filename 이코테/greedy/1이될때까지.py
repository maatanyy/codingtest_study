#나의 풀이, page 99, 그리디
x, y = map(int, input().split())

count = 0
while True:
    if x%y ==0:
        if x//y==1:
            count+=1
            break
        x=x//y
        count+=1
    else:
        x=x-1
        count+=1

print(count)

# 책의 풀이
#
# while x>=y:
#     while x%y!=0:
#         x-=1
#         count+=1
#     x//=y
#     count+=1
#
# while x>1:
#     y-=1
#     count+=1
#
# print(count)