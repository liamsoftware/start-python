from collections import deque

# Lists
a_list = ['one', 'two']
print(a_list)
a_list.append('three')
print(a_list)
a_list.insert(3, 'four')
print(a_list)

# List as stack
a_list.append('stackitem')
print(a_list)
a_list.pop()
print(a_list)

# List as queue
q = deque(a_list)
print(q)
q.append('queueitem')
print(q)
q.popleft()
print(q)
