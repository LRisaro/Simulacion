from math import floor

def generateRandomNumbers(a, c, m, times, u = 0):
  for i in range(times):
    u = (a*u + c) % m
    v = u / m
    # print('Iteration: ', i+1, ' Generated Number: ',  v)
    convertToFixedNumber(v)


def convertToFixedNumber(u):
  if (u <= .5):
    print('Generated Number: ', 1, ' Raw Number: ', u)
  elif (u > .5 and u <= .7):
    print('Generated Number: ', 2, ' Raw Number: ', u)
  elif (u > .7 and u <= .8):
    print('Generated Number: ', 3, ' Raw Number: ', u)
  elif (u > .8 and u <= 1):
    print('Generated Number: ', 4, ' Raw Number: ', u)

promPadron = floor((94335 + 93784) / 2)

generateRandomNumbers(1013904223, 1664525, 2**32, 100, promPadron)
