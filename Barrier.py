"""Барьер - противоположная семафору технология. Также указываем кол-во активных потоков.
Когда они запускаются, все дойдут до вызова метода wait()"""

import time
import random
import threading
from threading import currentThread


def test(barrier):
    slp = random.randint(3, 7)
    print(f'поток [{currentThread().name}] запущен в ({time.ctime()})')
    time.sleep(slp)

    barrier.wait()
    print(f'поток [{currentThread().name}] преодолел барьер в ({time.ctime()})')

bar = threading.Barrier(5)

for i in range(5):
    threading.Thread(target=test, args=(bar,), name=f'thr-{i}').start()