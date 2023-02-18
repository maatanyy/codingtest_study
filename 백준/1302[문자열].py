num = int(input())

book = dict()

for _ in range(num):
    i = str(input())
    if i not in book.keys():
        book[i]=1
    else:
        book[i]+=1

list = [k for k,v in book.items() if max(book.values())== v]
list.sort()
print(list[0])

