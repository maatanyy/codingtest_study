import itertools
import sys

n = int(input())

number_list = list(map(int,input().split()))
tool_list = list(map(int,input().split()))

tool = []

for i in range(4):
    if i==0:
        tool += ['+'] * tool_list[i]
    elif i==1:
        tool += ['-'] * tool_list[i]
    elif i==2:
        tool += ['*'] * tool_list[i]
    elif i==3:
        tool += ['%'] * tool_list[i]

check = []

for toools in list(set(itertools.permutations(tool))):
    val = number_list[0]

    for i in range(len(toools)):
        if toools[i]=='+':
            val+=number_list[i+1]

        elif toools[i]=='-':
            val-=number_list[i+1]

        elif toools[i]=='*':
            val*=number_list[i+1]

        elif toools[i]=='%':
            if val<0:
                val = abs(val) //number_list[i+1]
                val*=-1
            else:
                val//=number_list[i+1]

    check.append(val)
print(max(check))
print(min(check))

