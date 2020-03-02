from math import sqrt, log
from random import random
import numpy as np
import matplotlib.pyplot as plt

for n in range(100,1000000):
    narr.append(log(n))
    parr.append(log(pijak(n)))

plt.plot(np.array(narr), np.array(parr))
plt.show()

def pijak(n):
    k=1000
    tab=[]

    for i in range(k):
        x=0
        for j in range(n):    
            if random() < 0.5:
                x=x+1
            else:
                x=x-1
        tab.append(x)

    sum1=0
    sum2=0

    for i in range(k):
        sum1 = sum1+tab[i]
        sum2 = sum2+ tab[i]**2.

    x_sr = sum1/float(k)
    x2_sr = sum2/float(k)

    var = x2_sr - x_sr**2.

    stddev = sqrt(var)

    print (stddev)

    return stddev
