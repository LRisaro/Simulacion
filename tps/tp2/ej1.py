import numpy as np

def serviceCall():
  return np.random.exponential(1/4)

def distributedDBProcessTime():
  if (np.random.rand() <= 0.6):
    return np.random.exponential(10/7)
  else:
    return np.random.exponential(1)

def centralDBProcessTime():
  return np.random.exponential(10/8)
  
def meanInstantProcessedServiceCalls(waitTimes):
  return waitTimes.count(0) / len(waitTimes)

def simulateWaitTimes(processFn, times):
  serviceCallTime = 0
  readyAtTime = 0
  waits = list()
  solves = list()

  for i in range(0, times):
    serviceCallTime += serviceCall()
    processTime = processFn()
    waitTime = readyAtTime - serviceCallTime

    if (waitTime > 0):
      waits.append(waitTime)
      solves.append(waitTime + processTime)
    else:
      waits.append(0)
      solves.append(processTime)

    readyAtTime = serviceCallTime + processTime

  return { "waitTimes": waits, "solveTimes": solves }

def getTimeDiffPercent(t1, t2):
  wt1 = np.mean(t1)
  wt2 = np.mean(t2)
  return wt1*100/wt2

distributedTimes = simulateWaitTimes(distributedDBProcessTime, 100000)
centralTimes = simulateWaitTimes(centralDBProcessTime, 100000)

print('Tiempo medio de espera - 2 bases de datos distribuidas', np.mean(distributedTimes["waitTimes"]))
print('Tiempo medio de espera - 1 base de datos central', np.mean(centralTimes["waitTimes"]))

print('Fracción de solicitudes que no esperaron para ser procesadas - 2 bases de datos distribuidas', meanInstantProcessedServiceCalls(distributedTimes["waitTimes"]))
print('Fracción de solicitudes que no esperaron para ser procesadas - 1 base de datos central', meanInstantProcessedServiceCalls(centralTimes["waitTimes"]))

print('Tiempo medio de resolucion - 2 bases de datos distribuidas', np.mean(distributedTimes["solveTimes"]))
print('Tiempo medio de resolucion - 1 base de datos central', np.mean(centralTimes["solveTimes"]))

td = getTimeDiffPercent(distributedTimes["solveTimes"], centralTimes["solveTimes"])
print('La opcion de 2 bases de datos distribuidas es', td, '% de la opcion de 1 base de datos central')
if (td >= 50):
  print('Por lo tanto recomiendo la opcion de 1 base de datos central')
else:
  print('Por lo tanto recomiendo la opcion de 2 bases de datos distribuidas')

