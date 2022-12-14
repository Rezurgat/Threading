import time
import threading

value = 0

"""После результата работы создам объект блокировщика (Lock())"""

locker = threading.Lock()

"""Создам функцию,которая будет менять глобальную переменную value"""


def inc_value():
    global value
    while True:
        locker.acquire() #данный метод используется для блокировки последующих потоков к области ниже
        value += 1
        time.sleep(1)
        print(value)
        locker.release() #освобождает область выше и поток, который первый вызовет acquire() получит доступ к области выше

        """ Более коротка запись блокировщика -- with locker...."""

"""Создаю пять потоков, которые будут выполнять задачу по изменения глобальной переменной. В итоге 
получится хаос в ответе, что не есть хорошо. Для этого и существуют блокираторы (Lock и RLock).
RLock выполняет более жесткую блокировку. Через Lock() в любом режиме, любой поток может разблокировать для следующего
доступ к коду, что может быть чревато (через locker.release()). В таких случаях используется RLock()"""

for _ in range(5):
    threading.Thread(target=inc_value).start()