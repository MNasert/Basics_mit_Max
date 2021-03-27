import time
import numpy as np
import random

def handwrittenpyfunc(x):#wir schreiben mal alles per hand......
    rands = []
    for i in range(x):
        rands.append(random.random())
    q = 0
    for i in rands:
        q += i
    return q

def pyfunc(x):
    n = np.random.rand(x)#wir bedienen uns der einfachheit numpy
    n = sum(n)#und nehmen das was python direkt mitgibt! (ein builtin)
    return n

def numpyfunc(x):#und hier kommt numpy....
    n = np.random.rand(x)
    n = np.sum(n)
    return n

if __name__ == "__main__":
    start = time.time()
    handwrittenpyfunc(10000000)
    end = time.time()
    print("Die handwrittenpyfunc hat {}s gebraucht".format(end - start))
    #meh
    start = time.time()
    pyfunc(10000000)
    end = time.time()
    print("Die pyfunc hat {}s gebraucht".format(end-start))
    #nicht ganz so meh aber immer noch sehr meh
    start = time.time()
    numpyfunc(10000000)
    end = time.time()
    print("Die numpyfunc hat {}s gebraucht".format(end-start))
    #wow!