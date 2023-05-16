import sys

num = int(input())

graph = []

for _ in range(num):
    graph.append(list(input()))

flag = False
for i in range(num):
    for j in range(num):
        if graph[i][j] == '*':
            flag = True
            break

    if flag==True:
        break

t = i+1
v = j

count = 0
for k in range(0,v):
    if graph[t][k]=='*':
        count+=1

count2 = 0
for k in range(v+1,num):
    if graph[t][k]=='*':
        count2+=1

count3 = 0
for k in range(t+1,num):
    if graph[k][v]=='*':
        count3+=1

count4 = 0
for k in range(t+1, num):
    if graph[k][v-1]=='*':
        count4+=1

count5 = 0
for k in range(t+1, num):
    if graph[k][v+1]=='*':
        count5+=1

print(t+1,v+1)
print(count, count2, count3, count4, count5)
















