x, y, w, s = map(int,input().split())
# w 한블럭, s 대각선
ans = 0


if 2 * w >=s:

    ans = ans + min(x,y) *s

    temp = max(x,y) - min(x,y)

    if temp%2 == 0:

        tempcost = min(2*s, 2*w)
        ans = ans + tempcost * (temp//2)

    else:
        tempcost = min(2*s, 2*w)
        ans = ans + tempcost * (temp//2)
        ans = ans + w

else:

    ans += (x+y)*w

print(ans)