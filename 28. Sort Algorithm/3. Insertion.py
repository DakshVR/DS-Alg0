def insertionS(customL):
    for i in range(1, len(customL)):
        key = customL[i]
        j = i-1
        while j >= 0 and key < customL[j]:
            customL[j+1] = customL[j] 
        customL[j+1] = key
    print(customL)

cList = [4,7,2,8,9,1,3,5,6]
insertionS(cList)