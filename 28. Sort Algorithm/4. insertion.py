
#! Insertion Sort
#  Divide the given array into 2 parts.
#  Take first element from unsorted array and find its correct position in sorted aray
#  Repeat until unsorted array is empty


def Insertion(arr):                      #! ------------> TC = O(n^2), SC = O(1)
    for i in range(1, len(arr)):                       # ------------> TC = O(n)
        key = arr[i]                                   # ------------> TC = O(1)
        j = i-1                                        # ------------> TC = O(1)
        while j >=0 and key < arr[j]:                  # ------------> TC = O(n)
            arr[j+1] = arr[j]                          # ------------> TC = O(1)
            j -= 1                                     # ------------> TC = O(1)
        arr[j+1] = key                                 # ------------> TC = O(1)
    return arr                                         # ------------> TC = O(1)

arr = [3,5,6,7,2,8,1,4,9]
print(Insertion(arr))


#* When to use Insertion sort?
#  When we have insufficient memory
#  Easy to implement

#! When to avoid?

