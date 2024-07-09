
#! Bubble Sort

# Bubble sort is also referred as Sinking sort
# We repeatedly compare each pair of adjacent items and swap them if they are in the wron order.

def Bubble(arr):                         #! ------------> TC = O(n^2), SC = O(1)
    for i in range(len(arr)-1):                        # ------------> TC = O(n)
        for j in range(len(arr)-i-1):                  # ------------> TC = O(n)
            if arr[j] > arr[j+1]:                      # ------------> TC = O(1)
                arr[j], arr[j+1] = arr[j+1], arr[j]    # ------------> TC = O(1)
    return arr

arr = [3,5,6,7,2,8,1,4,9]
print(Bubble(arr))


#* When to use Bubble sort?
#   When the input is already sorted
#   Space is a concern
#   Easy to implement

#! When to avoid?
#   When time is taken into account, as average time complexity is poor.