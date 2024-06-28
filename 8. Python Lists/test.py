def first_second(my_list):
    # TODO
    my_list.sort()
    a = my_list[len(my_list)-1]
    b= my_list[len(my_list)-2]
    return a,b

list=[22,23,45,54,67,23,76,89,98,100,70,98]
print(first_second(list))