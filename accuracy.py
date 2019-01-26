#!/usr/bin/env python3
import os
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
import sys

def get_path(file, rel_path):

   script_dir = os.path.dirname(file)
   return os.path.join(script_dir, rel_path)

def main():
	try:
		truths = pd.read_csv(sys.argv[1], sep=',', index_col=0)
		predictions = pd.read_csv(sys.argv[2], sep=',', index_col=0)
		houses = {'Gryffindor': 0, 'Hufflepuff': 1, 'Ravenclaw': 2, 'Slytherin': 3}
		y_true = truths.replace(houses).values
		y_pred = predictions.replace(houses).values
		print("Your score on test set: {}%".format(100 * accuracy_score(y_true.reshape((400, )), y_pred.reshape((400, )))))
	except IndexError:
		print ("Usage : ./accuracy ours truth")
	except Exception as e:
		print ("Error " + str(e))
		sys.exit(1)


if __name__ == '__main__':
	main()
