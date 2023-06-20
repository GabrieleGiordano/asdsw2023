# See "Distributed Systems" - Van Steen, Tanenbaum - Ed. 4 (p. 117)

from multiprocessing import Process
from time import *
from random import *

"""
Notare la gestione della varaibile value. Al momento dello start, ciascun processo figlio ottiene una copia della
memoria del processo padre, quindi il valore attuale della variabile value (dentro al ciclo). Da questo momento in 
poi 
"""

global value

def sleeper(name):
    global value
    t = gmtime()
    s = randint(4,10)
    txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + name + ' is going to sleep for ' + str(s) + ' seconds '
    print(txt)
    sleep(s)
    t = gmtime()
    txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + name + ' has woken up ' + "la variabile vale " + str(value)
    print(txt)

if __name__ == '__main__':
    process_list = list()
    global value
    for i in range(10):
        t = gmtime()
        print("creazione processo",i," ",t.tm_min,":",t.tm_sec)
        p = Process(target=sleeper, args=('mike_{}'.format(i),))
        process_list.append(p)

    t = gmtime()
    print(f'tutti pronti {t.tm_min}:{t.tm_sec}')

    print("aspetto 2 secondi")
    sleep(2)
    for i, p in enumerate(process_list): 
        value = i
        t = gmtime()
        print("start processo",i, " ", t.tm_min, ":", t.tm_sec)
        p.start() #viene creata una copia delle risorse del processo padre, quindi una copia del valore attuale di value

    t = gmtime()
    print(f'tutti avviati {t.tm_min}:{t.tm_sec} e la variabile vale ancora {value}')

    for p in process_list: p.join()

    t = gmtime()
    print(f'tutti terminati! {t.tm_min}:{t.tm_sec}')
