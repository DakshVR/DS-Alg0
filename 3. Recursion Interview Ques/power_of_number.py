####################################################################################
#
#       How To Calculate Power Of Number
#
####################################################################################

def power(base, exponent):
    assert int(exponent) == exponent, 'Exponent should be Integer number only!'
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1/base * power(base, exponent+1)
    else:
        return base * power(base, exponent-1)


print(power(4, -1))
