mymap = []

for _ in range(5):
    mymap.append(list(map(int,input().split())))

mymap = sum(mymap,[])
check = []

for _ in range(5):
    check.append(list(map(int,input().split())))

check = sum(check,[])


bingoline = 0
time = 0


def check_bingo(array):
    count = 0

    if array[0]==array[5]==array[10]==array[15]==array[20]:
        count += 1

    if array[1]==array[6]==array[11]==array[16]==array[21]:
        count += 1

    if array[2]==array[7]==array[12]==array[17]==array[22]:
        count += 1

    if array[3]==array[8]==array[13]==array[18]==array[23]:
        count += 1

    if array[4]==array[9]==array[14]==array[19]==array[24]:
        count += 1

    if array[0] == array[1] == array[2] == array[3] == array[4]:
        count += 1

    if array[5] == array[6] == array[7] == array[8] == array[9]:
        count += 1

    if array[10] == array[11] == array[12] == array[13] == array[14]:
        count += 1

    if array[15] == array[16] == array[17] == array[18] == array[19]:
        count += 1

    if array[20] == array[21] == array[22] == array[23] == array[24]:
        count += 1

    if array[0] == array[6] == array[12] == array[18] == array[24]:
        count += 1

    if array[4] == array[8] == array[12] == array[16] == array[20]:
        count += 1

    return count


while True:
    time+=1
    val = check[0]
    index = mymap.index(val)
    mymap[index] = 99

    ans = check_bingo(mymap)

    if ans>=3:
        print(time)
        break

    check = check[1:]























