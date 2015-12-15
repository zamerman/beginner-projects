def fib(limit):
    x, y = 0, 1
    for i in range(1, limit):
        x, y = y, x + y
    return x
