import sys
x, y = map(int, sys.stdin.readline().split())

z = 100 * y // x

if z >= 99:
    print(-1)
else:
    start, end = 1, 1000000000

    while start<=end:
        middle = (start+end)//2
        if 100*(y+middle) // (x+middle) > z:
            end = middle-1
        else:
            start = middle+1

    print(end+1)