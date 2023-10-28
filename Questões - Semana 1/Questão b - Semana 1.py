import numpy as np
import math

somatorio = 0
n = 2
for n in range(n, 10000000):
    somatorio += 1/(n*((np.log(n))**2))
print(somatorio)