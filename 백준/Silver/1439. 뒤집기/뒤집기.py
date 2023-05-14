import sys
s = sys.stdin.readline()

Num1 = 0
Num2 = 0

for i in range(len(s) - 1) :
    if s[i] != s[i+1] and s[i] == "0" :
        Num2 += 1
    elif s[i] != s[i+1] and s[i] == "1" :
        Num1 += 1

print(min(Num1, Num2))