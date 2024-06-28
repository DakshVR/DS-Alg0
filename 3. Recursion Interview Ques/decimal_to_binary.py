####################################################################################
#
#       How To Convert Decimal To Binary
#
####################################################################################

def decimalToBinary(num):
    assert int(num) == num, 'The number has to be integer!'
    if num == 0:
        return 0
    else:
        # Why int(num/2) we need quotient as int
        return num % 2 + 10 * decimalToBinary(int(num/2))


print(decimalToBinary(1.3))
