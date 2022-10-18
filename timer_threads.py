import threading
import time

"""За таймеры отвечает time. time позволяет запускать потоки спустя заданное кол-во времени.
 Во время работы с таймером поток не блокируется. ПРосто ставлю таймер, ставлю поток в очередь 
 и продолжаю выполнение кода"""

def test():
    while True:
        print("test")
        time.sleep(1)

"""Использую класс Timer"""

#threading.Timer(10, test).start() # 10 - кол-во секунд, которое нужно ждать до запуска потока


"""Можно отменить поток до того, как он был запущен. Метод cancel()"""

thr = threading.Timer(5, test)
thr.start()

for _ in range(3):
    print('111')
    time.sleep(1)

thr.cancel()