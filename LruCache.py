

cache = []
capacity = 3


def add(item):
    if len(cache) == capacity:
        cache.pop(0)
    cache.append(item)


def out():
    print(cache)


out()
add(1)
add(2)
add(3)
out()
add(4)
add(4)
add(5)
add(4)
out()

