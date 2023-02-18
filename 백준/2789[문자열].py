val = str(input())

count = 0

for i in ('C','A','M','B','R','I','D','G','E'):
    val = val.replace(i,'')

print(val)