def fibonacci(n):
    assert n >= 0 and int(
        n) == n, 'Fibonnaci number cannot be negative number or non-integer! '
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = 5
print("the number is", fibonacci(n))
