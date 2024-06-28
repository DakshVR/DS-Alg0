####################################################################################
#
#  How To Find Sum Of Digits Of a Positive Integer
#  Number Using Recursion?
#
####################################################################################

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'Number cannot be negative or float int!'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n//10))


print(sumOfDigits(432234))
