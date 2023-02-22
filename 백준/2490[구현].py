for _ in range(3):
    temp = list(map(int,input().split()))
    num = temp.count(0)

    if num==0:
        print('E')
    if num == 1:
        print('A')
    if num == 2:
        print('B')
    if num ==3:
        print('C')
    if num ==4:
        print('D')