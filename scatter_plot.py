#!/usr/bin/env python

import csv
import sys
import math
import matplotlib.pyplot as plt

def check_ok(array):
	notempty = False
	for idx, val in enumerate(array):
		if (val != ""):
			notempty = True
			try:
				array[idx] = float(val)
			except:
				return (False)
	return (notempty)

def get_ana_from_table(array, name):
	if (not check_ok(array)):
		return False
	ret = []
	for a in array:
		ret.append(a)
	return ret


def get_analysis(array, fields):
	rez = []
	names = []
	for f in fields:
		if (f != "Index" and f != "Arithmancy"):
			tmp = []
			for dico in array:
				tmp.append(dico[f])
			tmp = get_ana_from_table(tmp, f)
			if (tmp != False):
				rez.append(tmp)
				names.append(f)
	return rez, names

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
dico = dict()

for r in reader:
	if (first == False):
		fields = r
		first = True
	else:
		i = 0
		for elem in r:
			dico[fields[i]] = elem
			i = i + 1
		array.append(dico.copy())

anal, names = get_analysis(array, fields)


plt.rcdefaults()
fig, ax = plt.subplots()

x_pos = range(1, len(names) + 2)

ax.set_xticks(x_pos)
ax.set_xticklabels(names)
ax.set_ylabel('Grades')
ax.set_xlabel('Subject')
ax.set_title('Pouet')

i = 1
for l in anal:
	for item in l:
		if (item != ""):
			plt.scatter(i, float(item))
	i += 1

print "here"
plt.show()
