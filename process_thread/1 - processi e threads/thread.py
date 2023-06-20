# See "Distributed Systems" - Van Steen, Tanenbaum - Ed. 4 (p. 118)

from multiprocessing import Process
from threading import Thread
from time import *
from random import *

def sleeping(name):
    global shared_x
    s = randint(1,20)
    sleep(s)
    shared_x = shared_x + 1

    t = gmtime()
    s = randint(1,20)
    txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + name + ' is going to sleep for ' + str(s) + ' seconds'
    print(txt)
    sleep(s)
    t = gmtime()
    txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + name + ' has woken up, seeing shared_x being ' + str(shared_x)
    print(txt)


def sleeper(name, num_thread):
    sleeplist = list()

    global shared_x
    shared_x = randint(10,99)

    for i in range(num_thread):
        subsleeper = Thread(target=sleeping, args=(name + ' th ' + str(i),))
        sleeplist.append(subsleeper)

    t = gmtime()
    txt = "pr " + name + 'initially sees shared_x being ' + str(shared_x) + f" at {t.tm_min}.{t.tm_sec}"
    print(txt)

    for s in sleeplist: s.start()
    for s in sleeplist: s.join()

    t = gmtime()
    txt = "pr " + name + 'finally sees shared_x being ' + str(shared_x) + f" at {t.tm_min}.{t.tm_sec}"
    print(txt)


   
if __name__ == '__main__':

    process_list = list()
    for i in range(4):
        process_list.append(Process(target=sleeper, args=('bob_' + str(i), randint(2,3),)))

    global x
    x = randint(10,99)

    t = gmtime()
    print(x," ",t.tm_min,":",t.tm_sec)

    for p in process_list: p.start()

    for p in process_list: p.join()

    t = gmtime()
    print(x," ",t.tm_min,":",t.tm_sec)
