# Idea: Define Fibonacci Sequence recursively, then use statement to break into cases: if num % 2 == 0, then total = total + x.

#def fib(n):
#    if n == 1:
#        return 1
#    elif n == 2:
#        return 2
#    return fib(n-1) + fib(n-2)


def fib(n):
    evens = 2
    low=1
    high=2
    while high <n:
        newNum = low + high
        if newNum % 2 == 0:
             evens += newNum
        low=high
        high=newNum
    return evens

print(fib(4000000))
