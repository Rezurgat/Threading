import time
import multiprocessing

"""Создам функцию, которая будет запускаться через процессы"""

def test():
    while True:
        print(f'{multiprocessing.current_process()}' time.time())
        time.sleep(1)

"""Для запуска процесса пишу следующее"""

multiprocessing.Process(target=test, name='prc-1')

"""Проверка, работает ли еще процесс"""

pr.is_alive()

"""id процесса"""

pr.pid

"""Убиваю процесс"""

pr.terminate()