import time
import threading

"""local() позволяет хранить данные в потоках и задавать нужные атрибуты, задавать
значения этим атрибутам. При использовании local() атрибут будет доступен только внутри потока"""

data = threading.local()

def get():
    print(data.value)

def t1():
    data.value = 111
    print('t1:', data.value)

def t2():
    data.test = 222
    print('t2:', data.test)

t1 = threading.Thread(target=t1).start()
t2 = threading.Thread(target=t2).start()