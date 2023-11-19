# 팬그램은 알파벳의 모든 글자를 사용하여 만든 문장을 말합니다.
# 공백이 없는 문자열이 주어졌을 때, 이 문자열이 팬그램인지 여부를 출력하는 프로그램을 작성해 주세요.
import sys
temp = input()

temp = temp.lower()

alpha = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,
         'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'y':0,'x':0,'z':0 }

for i in temp:
    alpha[i]+=1

for i in alpha.values():
    if i==0:
        print('NO')
        sys.exit()

print('YES')
