import time
from threading import Thread


def fun(number: int):
    print(f'fun {number} start ')
    time.sleep(1)
    print(f'fun {number} end')


start = time.perf_counter()
threads=[]
# thread1 = Thread(target=fun)
# thread2 = Thread(target=fun)
# thread3 = Thread(target=fun)
# thread4 = Thread(target=fun)
# # fun()
# # fun()
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()

for i in range(1, 100001):
    t = Thread(target=fun, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.perf_counter()

# print(f'start - {start}')
print(f'time is {end - start:0.2f}')
