def dictionary_example():
    print('Dictionary: key-value pairs, does not allow duplicate keys, add and remove operations')
    dic = {'c': '3', 'a': '1', 'b': '2'}
    print('original dictionary: ' + str(dic))
    dic['d'] = '4'
    dic['c'] = '5'
    print('added d and c (with dic[\'x\'] = \'y\'): ' + str(dic) + '\n')


def list_example():
    print('List: unordered, allows duplicates, add and remove operations')
    lis = ['one', 'two', 'three']
    print('original list: ' + str(lis))
    lis.append('four')
    lis.remove('one')
    print('list after append and remove operations: ' + str(lis) + '\n')


def set_example():
    print('Set: ordered, does not allow duplicates, add and remove operations')
    se = {'a', 'b', 'c'}
    print('original set: ' + str(se))
    se.add('a')
    print('added a (with add operation) but duplicate not allowed: ' + str(se))
    se.remove('c')
    print('removed c (with remove operation): ' + str(se) + '\n')


def tuple_example():
    print('Tuple: ordered and unchangeable collection')
    t = ('one', 'two', 'three')
    print('unchangeable tuple: ' + str(t) + '\n')


if __name__ == '__main__':
    dictionary_example()
    list_example()
    set_example()
    tuple_example()
