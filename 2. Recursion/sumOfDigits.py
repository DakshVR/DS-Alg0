def sum(n):
    if n == 1:
        return n
    return (sum(n//10) + int(n%10))

print(sum(1641))

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent <0:
        return 1/base * power(base, exponent-1)
    else:
        return base * power(base, exponent-1)
    

print(power(-3,4))

def greatestCommonDivisor(a, b):
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return greatestCommonDivisor(b, a%b)
    
print(greatestCommonDivisor(25,5))



def decimal2binary(n):
    if n == 0:
        return 1
    else:
        return (n%2 + 10 * decimal2binary(int(n/2)))
    
print(decimal2binary(13))


# Challenge

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1/base * power(base, exponent-1)
    else:
        return base * power(base, exponent-1)
    
def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

def productOfArray(arr):
    if len(arr) ==0:
        return 1
    else:
        return arr[0] * productOfArray(arr[1:])
    
def recursiveRange(num):
    if num == 0:
        return num
    else:
        return num + recursiveRange(num-1)


def fib(num):
    if num in [0,1]:
        return num
    else:
        return fib(num-1) + fib(num-2)