#!/usr/bin/env python

import projectile
import matplotlib.pyplot as plt
import numpy as np
import sys

fig = ""

if(len(sys.argv) == 1):
	fig = "../img/fig.png"
elif(len(sys.argv) > 2):
	print("Too many arguments")
else:
	fig = sys.argv[1]

p1 = projectile.IdealProjectile(30, 45)
p2 = projectile.ProjectileInMedium(30, 45, 0.450, 0.22)

xList1 = []
yList1 = []
xList2 = []
yList2 = []

for t in np.arange(0, p1.idealFlightTime, 0.05):

	xList1.append(p1.Inst_Param_Ideal(t)[0])
	yList1.append(p1.Inst_Param_Ideal(t)[1])

for t in np.arange(0, p2.realFlightTime, 0.05):

	xList2.append(p2.Inst_Param_Resistance(t)[0])
	yList2.append(p2.Inst_Param_Resistance(t)[1])

# Plotting using pyplot
plt.figure(1)
plt.plot(xList1, yList1, 'r', label='Projectile without air resistance')
plt.plot(xList2, yList2, 'c', label='Projectile with air resistance')
plt.xlim(0,100)
plt.ylim(0,50)
plt.title('Effect of drag on projectile motion')
plt.xlabel('Distance (in m)')
plt.ylabel('Height (in m)')
plt.legend()

# plt.figure(2)
# plt.plot(xList2, yList2)
# plt.xlim(0,100)
# plt.ylim(0,50)
# plt.xlabel('Distance (in m)')
# plt.ylabel('Height (in m)')

# plt.show()
plt.savefig(fig)
