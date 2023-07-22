e, s, m = map(int, input().split())

starte, starts, startm = 1, 1, 1
count = 1
#15,28,19

while True:
    if starte>15:
        starte = 1

    if starts >28:
        starts = 1

    if startm >19:
        startm = 1

    if starte == e and starts == s and startm==m:
        break

    count += 1
    starts += 1
    starte += 1
    startm += 1

print(count)
