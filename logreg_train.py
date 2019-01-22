#!/usr/bin/env python3

import csv
import sys
from math import *
import numpy as np

def sigmoid(x) :
	return (1. / (1. + np.exp(-x)))

def h(coef, features) :
	return sigmoid((np.transpose(coef) @ features)[0])

# def cost(data, coef, y):
# 	cost = 0.
# 	i = 0
# 	for features in data:
# 		print ("(y[i]) = " + str(type(1 - y[i])))
# 		print ("(features) = " + str((features)))
# 		print ("(log : ) = " + str(type(np.log(1. - h(coef, features)))))
# 		print ((1. - y[i]) * np.log(1. - h(coef, features)))
# 		cost += (y[i] * np.log(h(coef, features))) + ((1. - y[i]) * np.log(1. - h(coef, features)))
# 		print (cost)
# 		i += 1
# 	return (-cost / len(data))

def scale(tab):
	print (tab)
	min = np.ndarray.min(tab)
	max = np.ndarray.max(tab)
	if (min == max):
		min = 0
	for (i, f) in enumerate(tab):
		tab[i] = ((f - min) / (max - min)) * 2 - 1
	return (tab)

def	partial_derivative(j, data, coef, y):
	cost = 0
	for i, feature in enumerate(data):
		cost += (h(coef, feature) - y[i]) * feature[j]
	return (cost / len(feature))

if (len(sys.argv) != 2):
	print("Usage: " + sys.argv[0] + "file.csv")
	sys.exit()

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
y[y != "Slytherin"] = 0.
y[y == "Slytherin"] = 1.
y = y.astype(np.float64)

ar[ar == ''] = 0 # TODO ATTENTION AUX NANS
features = np.concatenate((np.ones((len(ar), 1)), ar[:, 6:].astype(np.float64)), axis=1)

for i in range(np.size(features,1)):
	features[ : , i] = scale(features[: , i])


print(y)
print(features)

coef = np.zeros((len(features[0]), 1))
print (coef)

learning_rate = .1
ok = .001
stop = False

while (not stop):
	tmp = coef.copy()
	stop = True
	for i, c in enumerate(coef):
		pd = partial_derivative(i, features, coef, y)
		# print("pd = " + str(pd))
		tmp[i] = tmp[i] - learning_rate * pd
		if (abs(tmp[i] - coef[i]) > ok):
			stop = False;
	coef = tmp
	print (coef)
	# print(coef[1])

print (coef)
np.save("coef.npy", coef)
