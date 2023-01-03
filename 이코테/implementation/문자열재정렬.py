# 아이디어는 잘 생각했는데 마지막에 이제 list를 str로 바꾸는 법을 몰라서 찾아봤다.
# 공뱁을 기준으로 print(''.join(리스트))로 변환한다는 것을 알게 되었다.
n = input()
sum =0
new =[]
for x in n:
    if x.isalpha():
        new.append(x)
    else:
        sum+=int(x)

new.sort()

if sum!=0:
    new.append(str(sum))

print(''.join(new))


