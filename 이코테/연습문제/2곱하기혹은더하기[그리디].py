n = str(input())

result = int(n[0])

for i in range(1,len(n)):
    val = int(n[i])
    if val <=1 or result<=1:
        result +=val

    else:
        result*=val

print(result)

