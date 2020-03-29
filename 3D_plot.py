# -*- coding: utf-8 -*-
"""
Created on 02/10/2020

@author: Timothee Klein
"""

import numpy as np
import csv
import os
import sys
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


with open('gasmap.item') as ItemFile:
    data = list(map(str, ItemFile))

data[:] = [line.rstrip('\n ') for line in data]

#Find Gas Map of Pressure Surface
GRSS02PR_line_nbr = data.index("GRSS02PR")
GTSS02PR_line_nbr = data.index("GTSS02PR")

PS = data[GRSS02PR_line_nbr+3 : GTSS02PR_line_nbr]

#Find Gas Map of Suction Surface
GRSS02SU_line_nbr = data.index("GRSS02SU")
GTSS02SU_line_nbr = data.index("GTSS02SU")

SS = data[GRSS02SU_line_nbr+3 : GTSS02SU_line_nbr]

#Convert list to array
PS_array_str = np.array(PS)
PS_array = PS_array_str.astype(np.str)

SS_array_str = np.array(SS)
SS_array = SS_array_str.astype(np.str)

#Cast as Float data type
PS_float = []
for i in range(0,len(PS_array)):
	line = np.fromstring(PS_array[i], dtype=float, sep=' ')
	PS_float = np.append(PS_float,line, axis=0) 

PS_float = np.reshape(PS_float, (len(PS_array), 3))
print(PS_float)

SS_float = []
for i in range(0,len(SS_array)):
	line = np.fromstring(SS_array[i], dtype=float, sep=' ')
	SS_float = np.append(SS_float,line, axis=0) 

PS_float = np.reshape(PS_float, (len(PS_array), 3))
print(PS_float)

SS_float = np.reshape(SS_float, (len(SS_array), 3))
print(SS_float)

#Parameters to be plotted
PS_AxialDistance = PS_float[:,0]
PS_RadialPosition = PS_float[:,1]
PS_Pressure = PS_float[:,2]

SS_AxialDistance = SS_float[:,0]
SS_RadialPosition = SS_float[:,1]
SS_Pressure = SS_float[:,2]

print(str('Suction Pressure:\n')+str(PS_Pressure))
print(str('Suction Axial Distance:\n')+str(PS_AxialDistance))
print(str('Suction Radial Position:\n')+str(PS_RadialPosition))
#Matplotlib graph
#Pressure Surface
fig = plt.figure(figsize=(15, 8),dpi=100)
ax1 = fig.add_subplot(121, projection='3d')
surf1=ax1.plot_trisurf(PS_AxialDistance, PS_RadialPosition, PS_Pressure, 
                cmap=cm.jet, vmin=min(SS_Pressure), vmax=max(PS_Pressure), 
                linewidth=0, antialiased=False)


# Add a color bar which maps values to colors.
fig.colorbar(surf1, shrink=0.5, aspect=15)
ax1.view_init(azim=-134, elev=50)
ax1.set_title('Pressure Surface')
ax1.set_xlabel('Axial (mm)')
ax1.set_ylabel('Radial (mm)')
ax1.set_zlabel('(MPa)')

#Suction Surface
ax2 = fig.add_subplot(122, projection='3d')
surf2=ax2.plot_trisurf(SS_AxialDistance, SS_RadialPosition, SS_Pressure, 
                cmap=cm.jet, vmin=min(SS_Pressure), vmax=max(PS_Pressure), 
                linewidth=0, antialiased=False)


# Add a color bar which maps values to colors.
#fig.colorbar(surf2, shrink=0.5, aspect=5)
ax2.view_init(azim=-134, elev=50)
ax2.set_title('Suction Surface')
ax2.set_xlabel('Axial (mm)')
ax2.set_ylabel('Radial (mm)')
ax2.set_zlabel('(MPa)')

plt.tight_layout()
fig.savefig('Plot.png',bbox_inches='tight', dpi=100)
plt.show()



