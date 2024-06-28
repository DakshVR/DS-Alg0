# ! Divide array into sorted and unsorted array
# Find min and swap it with first element

def selection(customL):

    for i in range(len(customL)):
        min_index = i
        for j in range(i+1, len(customL)):
            if customL[j] < customL[min_index]:
                min_index = j
        customL[i], customL[min_index] = customL[min_index], customL[i]
    print(customL)

cList = [4,7,2,8,9,1,3,5,6]
selection(cList)