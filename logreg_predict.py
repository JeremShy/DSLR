#!/usr/bin/env python3
import csv
import sys
from math import *
import numpy as np
#!/usr/bin/env python3

def sigmoid(x) :
	return (1. / (1. + np.exp(-x)))

def h(coef, features) :
	return sigmoid((np.transpose(coef) @ features)[0])

if (len(sys.argv) != 2):
	print("Usage: " + sys.argv[0] + "file.csv")
	sys.exit()

coef = np.load("coef.npy")
print (coef)



try:
	csvfile = open(sys.argv[1], 'r')
except:
	print("Error while trying to open " + sys.argv[1])
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
print(ar)

y = ar[ :, 1]
y[y != "Gryffindor"] = 0.
y[y == "Gryffindor"] = 1.
y = y.astype(np.float64)

ar[ar == ''] = 0 # TODO ATTENTION AUX NANS
features = np.concatenate((np.ones((len(ar), 1)), ar[:, 6:].astype(np.float64)), axis=1)

ok = 0
error = 0

for i, line in enumerate(features):
	if (h(coef, line) > .5):
		if (y[i] == 1):
			print ("[OK]")
			ok += 1
		else:
			print ("[ERROR]")
			error += 1
	else:
		if (y[i] == 0):
			print ("[OK]")
			ok += 1
		else:
			print ("[ERROR]")
			error += 1


print (("OK percentage : ") + str((ok / (ok + error)) * 100))
