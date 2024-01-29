s = input()
p= input()

idx = 0
answer = 0

while True:
    temp =''

    if s.find(p[idx:]) !=-1:
        answer+=1
        break

    for i in range(idx, len(p)):
        temp += p[i]

        if s.find(temp) ==-1:
            answer+=1
            idx = i
            break

print(answer)
