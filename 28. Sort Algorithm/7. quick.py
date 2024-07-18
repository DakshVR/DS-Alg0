
def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def pivot(my_list, pivotindex, end_index):
    swapindex = pivotindex 
    for i in range(pivotindex+1, end_index+1):
        if my_list[i] < my_list[pivotindex]:
            swapindex += 1
            swap(my_list, swapindex, i)
    swap(my_list, pivotindex, swapindex)
    return swapindex

def quicksort_helper(my_list, left, right):
    if left < right:
        pivotindex = pivot(my_list, left, right)
        quicksort_helper(my_list, left, pivotindex-1)
        quicksort_helper(my_list, pivotindex+1, right)
    return my_list

def quicksort(my_list):
    return quicksort_helper(my_list, 0, len(my_list)-1)

my_list = [3, 5, 0, 6, 2, 1, 4]
print(quicksort(my_list))
        