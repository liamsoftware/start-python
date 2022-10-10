from collections import deque


# Add to head of queue
# If queried, then add to head again
# Remove from the tail

class LruQueue:

    def __init__(self, size):
        self.queue = deque()
        self.size = size

    def add(self, item):
        if len(self.queue) > self.size:
            self.queue.popleft()
        self.queue.append(item)

    def is_cached(self, item):
        if item in self.queue:
            self.queue.remove(item)
            self.queue.append(item)
            return True
        else:
            return False

    def out(self):
        print(self.queue)


l = LruQueue(3)
l.add(1)
l.add(2)
l.add(3)
l.out()
l.add(4)
l.add(5)
l.is_cached(2)
l.add(6)
l.out()
