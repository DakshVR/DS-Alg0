# productOfArray([1,2,3]) #6
# productOfArray([1,2,3,10]) #60

def productOfArray(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] * productOfArray(arr[1:])


print(productOfArray([1, 2, 3, 4]))
