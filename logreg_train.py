#!/usr/bin/env python3

import csv
import sys
from math import *
import numpy as np

def sigmoid(x) :
	return (1. / (1. + np.exp(-x)))

def h(coef, features) :
	return sigmoid(features.T @ coef)

def update_coefs(features, y, coefs, lr):
	N = len(features)

	predictions = np.zeros(len(features))
	for i, f in enumerate(features):
		predictions[i] = h(coefs, f)
	gradient = np.dot(features.T, predictions - y)
	gradient /= N
	gradient *= lr
	coefs -= gradient
	return (coefs)


def scale(tab):
	# print (tab)
	min = np.ndarray.min(tab)
	max = np.ndarray.max(tab)
	if (min == max):
		min = 0
	for (i, f) in enumerate(tab):
		tab[i] = ((f - min) / (max - min)) * 2 - 1
	return (tab, min, max)

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
# print(ar)

ar[ar == ''] = 0 # TODO ATTENTION AUX NANS

features = np.concatenate((np.ones((len(ar), 1)), ar[:, 6:].astype(np.float64)), axis=1)
min = []
max = []
for i in range(np.size(features,1)):
	features[ : , i], t_min, t_max = scale(features[: , i])
	min.append(t_min)
	max.append(t_max)

to_save = {"min" : min, "max" : max}

for w in ["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"]:
	y = ar[ :, 1].copy()
	y[y != w] = 0.
	y[y == w] = 1.
	y = y.astype(np.float64)

	coef = np.zeros(len(features[0]))

	learning_rate = 1
	ok = .01
	stop = False

	while (not stop):
		tmp = coef.copy()
		tmp = update_coefs(features, y, tmp,learning_rate)
		if np.max(np.abs(coef - tmp)) < ok:
			stop = True
		coef = tmp
	print(coef)
	to_save[w] = coef

np.savez("params.npz", **to_save)
