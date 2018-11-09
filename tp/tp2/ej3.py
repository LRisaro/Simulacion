# 1) 2*xt = xt-1 + 2*yt-1
# 2) yt = yt-1 - xt-1/2
# 3) zt = zt-1 - xt-1 - yt-1
######################################################
# Entonces busco los puntos de equilibrio:
######################################################
# 1) xeq = xt = xt-1
# 2) yeq = yt = yt-1
# 3) zeq = zt = zt-1
######################################################
# Reemplazando:
######################################################
# 1) 2*xeq = xeq + 2*yeq
# 2) yeq = yeq - xeq/2
# 3) zeq = zeq - xeq - yeq
#
# 1) xeq = 2*yeq
# 2) xeq = 0, yeq = 0
######################################################
# Entonces los puntos de equilibrio del sistema son:
######################################################
# (xeq, yeq, zeq) = (0, 0, zeq), para todo zeq que pertenece a los reales
#

def dinSystem(p, times):
  o = p
  for i in range(0, times):
    x = (o[0] + 2*o[1]) / 2
    y = o[1] - o[0]/2
    z = o[2] - o[0] - o[1]
    o = [x, y, z]
    print(o)

x = [-1, 0, 1]
y = [-1, 0, 1]
z = [-1, 0, 1]

for i in x:
  for j in y:
    for u in z:
      # print(x[i], y[j], z[u])
      currentP = [x[i], y[j], z[u]]
      print("Calculando iteraciones para: ",currentP)
      dinSystem(currentP, 100)