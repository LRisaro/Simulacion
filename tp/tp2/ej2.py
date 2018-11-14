## 3 estados
# 1 - Esperando
# 2 - Arribo Solicitud
# 3 - Termina Proceso Solicitud
##
#     [ p11 p12 p13 ]   [ 113/120 1/40 1/30 ]
# P = [ p21 p22 p23 ] = [ 1 0 0 ]
#     [ p31 p32 p33 ]   [ 1 0 0 ]
import numpy as np

p = np.matrix([[113/120, 1/40, 1/30], [1, 0, 0], [1, 0, 0]])
stateChangeQ = round((1000 * 1000) / 10)

# Empieza esperando
currentState = [1, 0, 0]
stateCount = [0, 0, 0]
solCount = 0
stateNum = 1
for i in range(0, stateChangeQ):
  print('En estado ', stateNum, ':')
  stateCount[stateNum-1] += 1
  print(solCount, ' solicitudes en cola a los ', i*10, ' milisegundos')
  d = np.matmul(currentState, p**(i+1))
  probValues = d.tolist()[0]
  prob = np.random.uniform(0, 1)
  # print(probValues)
  if (prob <= probValues[0]):
    stateNum = 1
    currentState = [1, 0, 0]
  elif (prob <= (probValues[0] + probValues[1])):
    stateNum = 2
    currentState = [0, 1, 0]
    solCount += 1
  else:
    stateNum = 3
    currentState = [0, 0, 1]
    if (solCount > 0):
      solCount -= 1
      print('Solicitud procesada')
  print('')

print('En estado ', stateNum)
stateCount[stateNum-1] += 1
print(solCount, ' solicitudes en cola a los ', i*10, ' milisegundos')
print('Cantidad de veces en cada estado', stateCount)
