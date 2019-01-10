#!/usr/bin/env python

import csv
import sys
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import numpy as np

if (len(sys.argv) != 2):
	print ("Usage: " + sys.argv[0] + "file.csv")
	sys.exit()

try:
	csvfile = open(sys.argv[1], 'rb')
except:
	print ("Error while trying to open " + sys.argv[1])
	sys.exit()

reader = csv.reader(csvfile, delimiter=',')
first = False

array = []
for r in reader:
	if (first == False):
		fields = r
		first = True
	else:
		array.append(r)
ar = np.array(array)


nbr_features = len(array[0]) - 6
ar = np.array(array)
ar[ar == ''] = "nan" # TODO ATTENTION AUX NANS
color = ar[ : , 1].copy()

color[color == 'Ravenclaw'] = 'b'
color[color == 'Slytherin'] = 'g'
color[color == 'Gryffindor'] = 'r'
color[color == 'Hufflepuff'] = '#ffff00'
print (color)
# print ar[:, 6:]

g = ar[ar[:, 1] == "Gryffindor"][:, 6:].astype(np.float64)
s = ar[ar[:, 1] == "Slytherin"][:, 6:].astype(np.float64)
r = ar[ar[:, 1] == "Ravenclaw"][:, 6:].astype(np.float64)
h = ar[ar[:, 1] == "Hufflepuff"][:, 6:].astype(np.float64)

ar = ar[:, 6:].astype(np.float64)

# gs = gridspec.GridSpec(nbr_features, nbr_features)
# gs.update(wspace=0.025, hspace=0.05)

fig, ax = plt.subplots(nbr_features, nbr_features)
plt.subplots_adjust(wspace=0, hspace=0)
plt.setp(ax, xticks=[], yticks=[])

for i in range(0, nbr_features):
	for j in range(0, nbr_features):
		if (i == j):
			x = ar[:, i]
			x = x[~np.isnan(x)]
			ax[i][j].hist(x)
		else:
			ax[i][j].scatter(g[:, i], g[:, j], color='r', s=.1)
			ax[i][j].scatter(s[:, i], s[:, j], color='g', s=.1)
			ax[i][j].scatter(r[:, i], r[:, j], color='b', s=.1)
			ax[i][j].scatter(h[:, i], h[:, j], color='#ffff00', s=.1)

i = 0
for elem in ax[ : , 0]:
	elem.set_ylabel(fields[i + 6], rotation=0, labelpad=40, size='x-small')
	i = i + 1

i = 0
for elem in ax[nbr_features - 1, : ]:
	elem.set_xlabel(fields[i + 6], size='x-small')
	i = i + 1

# plt.figlegend(handles=[mpatches.Patch(color='r', label='Gryffindor'), mpatches.Patch(color='g', label='Slytherin'), mpatches.Patch(color='#ffff00', label='Hufflepuff'), mpatches.Patch(color='b', label='Ravenclaw')])

plt.show()
