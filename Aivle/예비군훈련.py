# 에이블 예비군 훈련
# 연차, 군별, 동원지정여부, 신분
#군별은 “ROKA”이면 육군, “ROKN”이면 해군, “ROKAF”이면 공군입니다.
#동원지정여부는 “Y”면 동원지정, “N”이면 동원미지정입니다.
#신분은 “Private”이면 병, “Officer”이면 간부입니다.
# - 간부의 경우,
#     - 0년차 동원미지정 육·해·공군 : 0시간
#     - 1~6년차 동원미지정 육·해·공군 : 28시간
#     - 1~6년차 동원지정 육·해·공군 : 28시간
# - 병의 경우,
#     - 0년차 동원미지정 육·해·공군 : 0시간
#     - 1~4년차 동원미지정 육·해군 : 32시간
#     - 1~4년차 동원지정 육·해·공군 및 1~4년차 동원미지정 공군 : 28시간
#     - 5~6년차 육·해·공군 동원미지정 : 20시간
# 0 ROKA N Private , 0
# 3 ROKN Y Private , 28

vals = input().split()

if str(vals[3]) == 'Private':
    if int(vals[0]) == 0 and str(vals[2])=='N':
        print(0)
        exit()

    elif int(vals[0]) >=1 and int(vals[0]) <=4 and str(vals[2])=='N' and (str(vals[1])=='ROKN' or str(vals[1])=='ROKA'):
        print(32)
        exit()

    elif (int(vals[0]) >=1 and int(vals[0]) <=4 and str(vals[2])=='Y') or (int(vals[0]) >=1 and int(vals[0]) <=4 and str(vals[2])=='N' and str(vals[1])=='ROKAF'):
        print(28)
        exit()

    elif (int(vals[0]) >=5 and int(vals[0]) <=6) and str(vals[2])=='N':
        print(20)
        exit()

elif str(vals[3]) == 'Officer':
    if int(vals[0]) == 0 and str(vals[2])=='N':
        print(0)
        exit()
    elif int(vals[0]) >=1 and int(vals[0]) <=6 and str(vals[2])=='N':
        print(28)
        exit()
    elif int(vals[0]) >=1 and int(vals[0]) <=6 and str(vals[2])=='Y':
        print(28)
        exit()