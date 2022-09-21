import time
from threading import Thread


def work():
    print('work thread begin')
    time.sleep(3)
    print('work thread complete')


t1 = Thread(target=work)
t1.start()

print('started another thread')
t1.join()
print('now main thread is complete')

# start multiple threads
threads = [Thread(target=work) for _ in range(5)]
[t.start() for t in threads]
