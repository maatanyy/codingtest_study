vals= input()


for i in range(len(vals)):
    
    if vals[i:] == vals[i:][::-1]:
        palin = vals + vals[:i][::-1]
        print(len(palin))
        break        