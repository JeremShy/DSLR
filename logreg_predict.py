#!/usr/bin/env python3
import csv
import sys
from math import *
import numpy as np
#!/usr/bin/env python3


def sigmoid(x) :
	return (1. / (1. + np.exp(-x)))

def h(coef, features) :
	return sigmoid(features.T @ coef)

def scale(tab, min, maxi):
	if (min == maxi):
		min = 0
	for (i, f) in enumerate(tab):
		tab[i] = ((f - min) / (maxi - min)) * 2 - 1
	return (tab)


def get_coef(student, coef_g, coef_r, coef_s, coef_h):
	guess_g = h(coef_g, student)
	guess_r = h(coef_r, student)
	guess_s = h(coef_s, student)
	guess_h = h(coef_h, student)

	print ("guess_g : " + str(guess_g))
	print ("guess_r : " + str(guess_r))
	print ("guess_s : " + str(guess_s))
	print ("guess_h : " + str(guess_h))
	print ("")

	ok = max(guess_g, guess_r, guess_s, guess_h)
	if (ok == guess_g):
		return ("Gryffindor")
	elif (ok == guess_r):
		return ("Ravenclaw")
	elif (ok == guess_s):
		return ("Slytherin")
	elif (ok == guess_h):
		return ("Hufflepuff")

if (len(sys.argv) != 2):
	print("Usage: " + sys.argv[0] + "file.csv")
	sys.exit()

coef_g = np.load("Gryffindor_coef.npy")
coef_r = np.load("Ravenclaw_coef.npy")
coef_s = np.load("Slytherin_coef.npy")
coef_h = np.load("Hufflepuff_coef.npy")
min = np.load("min.npy")
maxi = np.load("max.npy")


print (coef_g)
print (coef_r)
print (coef_s)
print (coef_h)

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

ar[ar == ''] = 0 # TODO ATTENTION AUX NANS

features = np.concatenate((np.ones((len(ar), 1)), ar[:, 6:].astype(np.float64)), axis=1)

for i in range(np.size(features,1)):
	features[ : , i] = scale(features[: , i], min[i], maxi[i])

ok = 0
error = 0
student = []

for i, line in enumerate(features):
	student.append(get_coef(line, coef_g, coef_r, coef_s, coef_h))

for i, line in enumerate(features):
	guess = get_coef(line, coef_g, coef_r, coef_s, coef_h)
	if (guess == y[i]):
		print ("[OK]")
		ok += 1
	else:
		print ("[ERROR] : expected {" + str(y[i])+ "} got {" + guess + "}")
		error += 1


print (("OK percentage : ") + str((ok / (ok + error)) * 100))
