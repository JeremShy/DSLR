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
	ret = {"Count": 0.0, "Mean": 0.0, "Std": 0.0, "Min": array[0], "25%": 0.0, "50%": 0.0, "75%": 0.0, "Max": array[0], "tot": 0.0, "name": name}
	ret = find_first_values(array, ret)
	array.sort()
	if (ret["Count"] % 2 == 1):
		ret["50%"] = array[int(ret["Count"] / 2)]
	else:
		ret["50%"] = (array[int(ret["Count"] / 2) - 1] + array[int(ret["Count"] / 2)]) / 2
	if (ret["Count"] % 4 == 0):
		ret["25%"] = array[int(ret["Count"] / 4 - 1)]
 		ret["75%"] = array[int(ret["Count"] / 4 * 3 - 1)]
	else:
		ret["25%"] = array[int(ret["Count"] / 4)]
		ret["75%"] = array[int(ret["Count"] / 4 * 3)]

	tot = 0
	for val in array:
		if (val == ""):
			continue
		tot += (val - ret["Mean"]) * (val - ret["Mean"])
	tot = tot / (ret["Count"])
	ret["Std"] = math.sqrt(tot)
	del ret["tot"]
	return ret


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
