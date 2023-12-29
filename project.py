import matplotlib.pyplot as plt
import math
import numpy as np

e = 1.6*10**(-19)
m = 9.1*10**(-31)
fig, ax = plt.subplots()
with open("data.txt") as f:
    B, U, ra, p0, vr0, vp0, vz0, j, g = map(float, f.readline().split())
    h = 10**j
    n = int(10**g)
    U = int(U)

rk = ra/10
r = [rk]
p = [p0]
vr = [vr0]
vp = [vp0]
x = [r[-1]*math.cos(p[-1])]
y = [r[-1]*math.sin(p[-1])]
z = [0]
# v = []
for k in range(n):
    rn = r[-1] + h*vr[-1]
    if rn < ra and rn >= rk:
        vr.append(vr[-1] + h*e/m*(-vp[-1]*B + U/(np.log(ra/rk)*r[-1])))
        p.append(p[-1] + h*vp[-1]/r[-1])
        vp.append(vp[-1] + h*e*B*vr[-2]/m)
        r.append(rn)
        # v.append(math.sqrt(vr[-1]**2 + vp[-1]**2))
        x.append(r[-1]*math.cos(p[-1]))
        y.append(r[-1]*math.sin(p[-1]))
        z.append(z[-1] + h*vz0)
    else:
        break

#oxy
plt.subplot(1, 2, 1)
angle = theta = np.linspace( 0 , 2 * np.pi , 150 )
rxa = ra*np.cos(angle)
rya = ra*np.sin(angle)
plt.plot(rxa, rya)
rxk = rk*np.cos(angle)
ryk = rk*np.sin(angle)
plt.plot(rxa, rya, color="b")
plt.plot(rxk, ryk, color="b")
plt.plot(x, y)
plt.title("Проекция на Oxy\n" + f"B = {B}, U = {U}", fontdict={"size":15})
plt.xlabel("Ox, м", fontdict={"size":15})
plt.ylabel("Oy, м", fontdict={"size":15})
plt.grid()

#oxz
plt.subplot(1, 2, 2)
plt.plot(x, z)
plt.axvline(x = ra, color = 'b')
plt.axvline(x = -ra, color = 'b')
plt.axvline(x = rk, color = 'b')
plt.axvline(x = -rk, color = 'b')
plt.title("Проекция на Oxz\n" + f"B = {B}, U = {U}", fontdict={"size":15})
plt.xlabel("Ox, м", fontdict={"size":15})
plt.ylabel("Oz, м", fontdict={"size":15})
plt.grid()

#ax.plot(range(len(v)), v)
plt.show()