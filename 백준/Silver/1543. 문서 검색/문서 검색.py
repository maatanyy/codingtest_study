text = str(input())
findtext = str(input())
count = 0

while True:
    if text.find(findtext)!=-1:
        count+=1
        text = text.replace(findtext,'---',1)

    else:
        break

print(count)
