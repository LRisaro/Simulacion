import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
from math import sqrt, exp, pi, log

c = sqrt(2*exp(1)/pi)

n = 100000
aceptados = list() #VALORES ACEPTADOS SEGUN DISTRIBUCIÓN NORMAL, MEDIA 35 Y DESVÍO 5

#NORMAL DE MEDIA 35 Y VARIANZA 25
def X(t):
    return exp(-0.5*t)/(sqrt(2*pi))
    # return exp(-0.5*(((t-35)/5)**2))/(5*sqrt(2*pi))

def Y(t):
    return exp(-t)

def prob(t):
    return (X(t)/(c*Y(t)))

def transformL(x, a, b):
    return (x*a) + b

count = 1
maxAceptado = 100000
while count <= maxAceptado:
    u = np.random.uniform()
    j = np.random.exponential(1)

    if(u < prob(j)):
        # print('aceptado: ', count)
        count += 1
        if(np.random.rand() < 0.5):
            aceptados.append( transformL(j, 3, 35) )
            # aceptados.append(j)
        else:
            aceptados.append( transformL(j*-1, 3, 35) )
            # aceptados.append((-1*j))

print('Varianza = ' + str(np.var(aceptados)))
print('Media = ' + str(np.median(aceptados)))
print('Moda = ' + str(st.mode(aceptados)[0][0]))


valoresNormal = list()
for i in range(0, maxAceptado):
    n = np.random.normal(35, 5)
    valoresNormal.append(n)

print('Varianza = ' + str(np.var(valoresNormal)))
print('Media = ' + str(np.median(valoresNormal)))
print('Moda = ' + str(st.mode(valoresNormal)[0][0]))
