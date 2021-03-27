import numpy as np
import random
import time
#wir schreiben zweimal die selbe methode
def pyfunc(x):
    rands = []
    for i in range(x):
        rands.append(random.random())
    return rands

def numpyfunc(x):
    rands = np.random.random(x)
    return rands

#testen wie gehabt
if __name__ == "__main__":
    start = time.time()
    pyfunc(10000000)
    end = time.time()
    print("Die pyfunc hat {}s gebraucht".format(end-start))

    start = time.time()
    numpyfunc(10000000)
    end = time.time()
    print("Die numpyfunc hat {}s gebraucht".format(end-start))