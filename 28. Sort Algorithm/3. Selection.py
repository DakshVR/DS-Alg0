
#! Selection Sort
#  In case of selection sort we repearedly find the minimum element and move it to the sorted part of the array to make unsorted part sorted.

#* It works best for small array, and it doesn't require additional space.

def Selection(arr):                      #! ------------> TC = O(n^2), SC = O(1)
    for i in range(len(arr)):                          # ------------> TC = O(n)
        minIndex = i                                   # ------------> TC = O(1)
        for j in range(i+1, len(arr)):                 # ------------> TC = O(n)
            if arr[minIndex] > arr[j]:                 # ------------> TC = O(1)
                minIndex = j                           # ------------> TC = O(1)
        arr[i], arr[minIndex] = arr[minIndex], arr[i]  # ------------> TC = O(1)
    return arr                                         # ------------> TC = O(1)

arr = [3,5,6,7,2,8,1,4,9]
print(Selection(arr))

#* When to use Selection sort?
#  When we have insufficient memory
#  Easy to implement
#  When we have continuous inflow of numbers and we want to keep them sorted

#! When to avoid?
#  When time is a concern
