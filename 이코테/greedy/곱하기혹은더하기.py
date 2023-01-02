#page 312
# 접근은 잘했으나 약간 고민했다. 두번쨰 수를 받아서 비교하는 부분을 더 보완할 필요!
n = str(input())

num = int(n[0])
for i in range(1, len(n)):
   if int(n[i]) <=1 or num<=1:
       num+=int(n[i])
   else:
       num*=int(n[i])
print(num)
