num = int(input())

d = [0]*1000

d[1] = 1
d[2] = 3

for i in range(3,num+1):
    d[i] = (d[i-1]+ 2 * d[i-2]) % 796796

print(d[num])