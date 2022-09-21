# Pass by reference - the address of the object in memory is passed to the method.
# Pass by value - a copy of the object is passed to the method.

# Python is pass by reference.
# The below example shows that the original list is updated by the method.

def change_object(a_list):
    a_list.append('another item')
    a_list.append('another item again')


my_original_list = ['item1', 'item2']
print(my_original_list)
change_object(my_original_list)
print(my_original_list)
