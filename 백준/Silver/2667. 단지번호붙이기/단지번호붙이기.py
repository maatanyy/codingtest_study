check = 123456789
num = int(input())

graph = []
val = []
for i in range(num):
    graph.append(list(map(int, input())))

def dfs(x,y):

    if x<=-1 or x>=num or y<=-1 or y>=num:
        return False

    if graph[x][y] == 1:
        global count
        count+=1
        graph[x][y] = check
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True

    return False

result =0
count = 0

for i in range(num):
    for j in range(num):
        if dfs(i,j) == True:
            val.append(count)
            result+=1
            count=0

print(result)
val.sort()
for i in range(len(val)):
    print(val[i])


