def fib(x):

    if x==1 or x==2:
        return 1
    else:
        return fib(x-1) + fib(x-2)

x =int(input())
print(fib(x))
