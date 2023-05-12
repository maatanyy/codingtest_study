import sys

check = 'aeiou'

while True:

    text = str(input())

    if text=='end':
        break

    Flag = True

    if 'a' in text or 'e' in text or 'i' in text or 'o' in text or 'u' in text:
        jaum = 0
        moum = 0
        val =''

        for i in range(len(text)):
            if text[i] not in check:
                jaum += 1
                moum = 0

                if jaum>=3:
                    Flag = False
                    break

                if val == text[i]:
                    Flag = False
                    break

            else:
                jaum = 0
                moum +=1

                if moum>=3:
                    Flag = False
                    break

                if val == text[i]:
                    if text[i]!='e' and text[i]!='o':
                        Flag = False
                        break

            val = text[i]

        if Flag==False:
            print(f'<{text}> is not acceptable.')

        elif Flag==True:
            print(f'<{text}> is acceptable.')


    else:
        print(f'<{text}> is not acceptable.')













