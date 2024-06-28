####################################################################################
#
#           How To Finf Greatest Common Divisor Of Two Numbers
#
####################################################################################

def gcd(num1, num2):
    assert int(num1) == num1 and int(
        num2) == num2, 'The Numbers must be Integers!'
    if num1 < 0:
        num1 = -1 * num1
    if num2 < 0:
        num2 = -1 * num2
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


print(gcd(48, 18))
