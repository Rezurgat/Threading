""" Метод join позволяет дождаться выполнения моего потока"""

import time
import threading


def get_data(data, value):
    for _ in range(value):
        print(f'[{threading.currentThread().name}] - {data}')
        time.sleep(1)


""" Создаю список, в котором буду хранить объекты всех потоков """

thr_list = []

""" Создаю еще 3 потока для проверки """


for i in range(3):
    thr = threading.Thread(target=get_data, args=(str(time.time()), i,), name=f'thr-{i}') # i есть value
    thr_list.append(thr)
    thr.start()

""" Создав список, я могу в последствии обращаться к каждому из потоков и управлять ими.
 В цикле при использовании join я сначала дождусь выполнения всех потоков и только потом
начнет выполняться код который идет после join() (после цикла)"""

for i in thr_list:
    i.join()