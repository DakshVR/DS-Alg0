from question import LinkedList

def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head
    for i in range(n):
        