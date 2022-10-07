import time
import threading


""" Пишу функцию,которую буду запускать через поток """


def get_data(data):
    thr_name = "aa"
    print(f'[{thr_name}] - {data}')
    time.sleep(5)

""" Использую поток, где target - адрес на объект (функцию), name - название потока,
args=() - аргументы ф-ии (можно через kwargs), daemon или обычный поток"""

threading.Thread(target=get_data(), args=(str(time.time())),).start()