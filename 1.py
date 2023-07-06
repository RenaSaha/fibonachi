def get_fib_numbers(qty):

    f = 0
    y = 1
    a = [0]
    while qty-1 > 0:
        c = f + y
        y = f
        f = c
        qty -= 1
        a.append(c)

    return a


fib = get_fib_numbers(10)
print(fib)