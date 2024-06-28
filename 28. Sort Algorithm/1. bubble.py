
# !   When TO Use Bubble Sort?
#   When the input is already sorted
#   when Space is Concern, as it is in place sorting
#   Easy to implement

# !  When to avoid

#  When time complexity is a factor, as it takes O(n^2)

def bubblesort(customList):
    length = len(customList)-1
    for i in range(length):
        for j in range(length-i):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1],customList[j]
    
    print(customList)

cList = [4,7,2,8,9,1,3,5,6]
bubblesort(cList)