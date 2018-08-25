#!/usr/bin/env python

import csv
import sys
import math
import matplotlib.pyplot as plt
import numpy as np

if (len(sys.argv) != 2):
	print "Usage: " + sys.argv[0] + "file.csv"
	sys.exit()

try:
	csvfile = open(sys.argv[1], 'rb')
except:
	print "Error while trying to open " + sys.argv[1]
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
print ar

plt.rcdefaults()
fig, ax = plt.subplots()

ar[ar == ''] = "nan" # TODO ATTENTION AUX NANS

astronomy = ar[: , fields.index("Astronomy")].astype(float)
defense = ar[: , fields.index("Defense Against the Dark Arts")].astype(float)
plt.scatter(astronomy, defense, s=0.5)

print (len(astronomy))
print (len(defense))
print "here"

ax.set_ylabel('Defense Against The Dark Arts')
ax.set_xlabel('Astronomy')
ax.set_title('Quelles sont les deux features qui sont semblables ?')
plt.show()
