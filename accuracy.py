#!/usr/bin/env python3
import os
import pandas as pd
from sklearn.metrics import accuracy_score
import sys

def main():
	try:
		truths = pd.read_csv(sys.argv[1], sep=',', index_col=0)
		predictions = pd.read_csv(sys.argv[2], sep=',', index_col=0)
		houses = {'Gryffindor': 0, 'Hufflepuff': 1, 'Ravenclaw': 2, 'Slytherin': 3}
		y_true = truths.replace(houses).values
		y_pred = predictions.replace(houses).values
		print("Your score on test set: {}%".format(100 * accuracy_score(y_true.reshape((len(y_true), )), y_pred.reshape((len(y_true), )))))
	except IndexError:
		print ("Usage : ./accuracy ours truth")
	except Exception as e:
		print ("Error " + str(e))
		sys.exit(1)


if __name__ == '__main__':
	main()
