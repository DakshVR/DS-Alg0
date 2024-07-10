
import math

#! Bucket Sort
#  Create buckets and distribute elements of array into buckets.
#  Sort buckets individually
#  merge buckets after sorting.

#* Number of buckets = round(sqrt(number of elements))

#? how to determine which bucket to insert element in.
#* Appropriate bucket = ceil( Value * number of buckets / maxvalue)

def insertionsort(arr):                  #! ------------> TC = O(n^2), SC = O(1)
    for i in range(1, len(arr)):                       # ------------> TC = O(n)
        key = arr[i]                                   # ------------> TC = O(1)
        j = i-1                                        # ------------> TC = O(1)
        while j >=0 and key < arr[j]:                  # ------------> TC = O(n)
            arr[j+1] = arr[j]                          # ------------> TC = O(1)
            j -= 1                                     # ------------> TC = O(1)
        arr[j+1] = key                                 # ------------> TC = O(1)
    return arr                                         # ------------> TC = O(1)
 
def bucket(arr):                         #! ------------> TC = O(n^2), SC = O(N)
    numberOfBuckets = round(math.sqrt(len(arr)))
    maxvalue = max(arr)
    temp = []

    for i in range(numberOfBuckets):                   # ------------> TC = O(n)
        temp.append([])

    for j in arr:
        index_b = math.ceil(j * numberOfBuckets / maxvalue)
        temp[index_b-1].append(j)
    
    for i in range(numberOfBuckets):
        temp[i] = insertionsort(temp[i])  # USe QUICK # ------------> TC = O(n)
    
    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(temp)):
            arr[k] = temp[i][j]
            k += 1

    return arr

arr = [3,5,6,7,2,8,1,4,9]
print(bucket(arr))

#* When to use Bucket sort?
#  When input is uniformly distributed over range

#! When to avoid?
#  When space is concern

