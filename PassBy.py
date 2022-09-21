# Pass by reference - the address of the object in memory is passed to the method.
# Pass by value - a copy of the object is passed to the method.

# Python is pass by reference.
# The below example shows that the original list is updated by the method.

def change_list(a_list):
    a_list.append('another item')
    a_list.append('another item again')


my_original_list = ['item1', 'item2']
print(my_original_list)
change_list(my_original_list)
print(my_original_list)


def change_another_list(a_list):
    a_list = ['new', 'list']


change_another_list(my_original_list)
print(my_original_list)


def change_another_list_wtih_return(a_list):
    a_list = ['a', 'new', 'list']
    return a_list


my_original_list = change_another_list_wtih_return(my_original_list)
print(my_original_list)