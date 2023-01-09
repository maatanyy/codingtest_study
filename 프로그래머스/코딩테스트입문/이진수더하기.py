def solution(bin1, bin2):
    answer = ''
    temp, temp2 = 0, 0
    for i in range(len(bin1)):
        temp+= pow(2,i) *int(bin1[-(i+1)])

    for i in range(len(bin2)):
        temp2+= pow(2,i) *int(bin2[-(i+1)])

    value = temp+temp2
    value = format(value,'b')
    answer = str(value)

    return answer

bin1 = "10"
bin2 = "11"

solution(bin1,bin2)