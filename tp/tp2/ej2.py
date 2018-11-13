## 3 estados
# 1 - Esperando
# 2 - Arribo Solicitud
# 3 - Termina Proceso Solicitud
##
#     [ p11 p12 p13 ]   [ 113/120 1/40 1/30 ]
# P = [ p21 p22 p23 ] = [ 1 0 0 ]
#     [ p31 p32 p33 ]   [ 1 0 0 ]
import numpy as np

matrix = np.matrix([[113/120, 1/40, 1/30], [1, 0, 0], [1, 0, 0]])
stateChangeQ = round((1000 * 1000) / 10)
# stateCount = [Esperando, Arribo Solicitud, Termina Proceso Solicitud]
stateCount = [0, 0, 0]

print(matrix)
print(stateChangeQ)

# Empieza esperando
stateCount[0] += 1
currentState = np.matrix([[1, 0, 0]])

for i in range(0, 3):
  prob = np.random.uniform(0, 1)
  if (prob <= 113/120):
    currentState = np.matrix([[1, 0, 0]])
  else if (prob <= 29/30):
    currentState = np.matrix([[0, 1, 0]])
  else:
    currentState = np.matrix([[0, 0, 1]])
