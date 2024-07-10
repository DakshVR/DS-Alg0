
#! Merge Sort

# Merge sort is a Divide and Conqure algorithm
# Divide the input array in two halves and we keep halving recursively until they become too small that cannot be broken further
# Merge halves by sorting them.

def Merge(customList, left, mid, right):  #! ------------> TC = O(n), SC = O()
    num1 = mid - left + 1
    num2 = right - mid

    Leftarr = [0] * num1
    Rightarr = [0] * num2

    for i in range(0, num1):
        Leftarr[i] = customList[left + i]
    
    for j in range(0, num2):
        Rightarr[j] = customList[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < num1 and j < num2:
        if Leftarr[i] <= Rightarr[j]:
            customList[k] = Leftarr[i]
            i += 1
        else:
            customList[k] = Rightarr[j]
            j += 1
        k += 1
    
    while i < num1:
        customList[k] = Leftarr[i]
        i += 1
        k += 1

    while j < num2:
        customList[k] = Rightarr[j]
        j += 1
        k += 1


def mergesort(customList, left, right):#! ------------> TC = O(NLogn), SC = O(N)
    if left < right:
        mid = (left + (right - 1)) //2
        mergesort(customList, left, mid)        # ------------> TC = O(n/2)
        mergesort(customList, mid+1, right)     # ------------> TC = O(n/2)
        Merge(customList, left, mid, right)     # ------------> TC = O(n)
    
    return customList

arr = [3,5,6,7,2,8,1,4,9]
print(mergesort(arr, 0, len(arr)-1))


#* When to use Merge sort?
#   Better than selection or insertion, faster then them
#   When you need stable sort
#   When average expected time is O(NlogN)

#! When to avoid?
#   When space is concern.