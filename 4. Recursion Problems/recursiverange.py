# recursiveRange(6) # 21
# recursiveRange(10) # 55


def recursiveRange(num):
    if num == 1:
        return 1
    else:
        return num + recursiveRange(num-1)


print(recursiveRange(6))
