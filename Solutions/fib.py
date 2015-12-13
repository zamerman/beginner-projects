# Fibbonacci Sequence
# Python 3.5.1
# Written by alfredmuffin

def fib(limit):
    x, y = 0, 1
    for i in range(1, limit):
        x, y = y, x + y
    return x
