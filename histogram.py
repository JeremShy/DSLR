#!/usr/bin/env python

import csv
import sys
import math
import matplotlib.pyplot as plt

def check_ok(array):
	notempty = False
	for idx, dic in enumerate(array):
		for house, val in dic.items():
			if (val != ""):
				notempty = True
				try:
					array[idx] = {house: float(val)}
				except:
					return (False)
	return (notempty)

def get_val(ls, fields):
	if (check_ok(ls) == False):
		return (False, 0)
	print fields + " for in get val"
	rez = {}
	rez["Gryffindor"] = {"tot" : 0.0, "mean" : 0.0, "count" : 0.0}
	rez["Slytherin"] = {"tot" : 0.0, "mean" : 0.0, "count" : 0.0}
	rez["Hufflepuff"] = {"tot" : 0.0, "mean" : 0.0, "count" : 0.0}
	rez["Ravenclaw"] = {"tot" : 0.0, "mean" : 0.0, "count" : 0.0}
	for d in ls:
		for house, val in d.items():
			if (house == "Gryffindor" or house == "Slytherin" or house == "Hufflepuff" or house == "Ravenclaw"):
				if (val != ""):
					rez[house]["tot"] += float(val)
					rez[house]["count"] += 1
	for r in rez:
		if (rez[r]["count"] != 0):
			rez[r]["mean"] = rez[r]["tot"] / rez[r]["count"]
	mean = (rez["Gryffindor"]["mean"] + rez["Slytherin"]["mean"] + rez["Hufflepuff"]["mean"] + rez["Ravenclaw"]["mean"]) / 4
	std = (rez["Gryffindor"]["mean"] - mean) * (rez["Gryffindor"]["mean"] - mean)
	std += (rez["Slytherin"]["mean"] - mean) * (rez["Slytherin"]["mean"] - mean)
	std += (rez["Hufflepuff"]["mean"] - mean) * (rez["Hufflepuff"]["mean"] - mean)
	std += (rez["Ravenclaw"]["mean"] - mean) * (rez["Ravenclaw"]["mean"] - mean)
	std /= 4
	std = math.sqrt(std)
	return (True, std)

def get_analysis(array, fields):
	rez = []
	names = []
	for f in fields:
		if (f == "Index"):
			continue
		tmp = []
		for dico in array:
			tmp.append({dico["Hogwarts House"] : dico[f]})
		b, tmp = get_val(tmp, f)
		if (b != False):
			print tmp
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
print anal
print names

plt.rcdefaults()
fig, ax = plt.subplots( figsize=(35, 12))

x_pos = range(len(names))

ax.bar(x_pos, anal, align='center')
ax.set_xticks(x_pos)
ax.set_xticklabels(names)
ax.set_ylabel('Standard deviation')
ax.set_xlabel('Subject')

ax.set_title('Quel cours de Poudlard a une repartition des notes homogenes entre les quatres maisons ?')

plt.show()
