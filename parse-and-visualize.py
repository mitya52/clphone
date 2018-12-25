#!/usr/bin/python3
import matplotlib.pyplot as plt
import pandas as pd

def visualize(data, maxx=None):
	data = data[data.price.apply(lambda x: x != 'price')]
	data = data.astype('int')
	if maxx:
		data = data[data.price.apply(lambda x: x < maxx)]
	data.hist(bins=200)
	print('mean (< {}): {}'.format(maxx, data.price.mean()))
	plt.show()

if __name__ == '__main__':
	import sys

	if len(sys.argv) != 2:
		print('Using: {} prices.csv'.format(sys.argv[0]))
		exit(1)

	data = pd.read_csv(sys.argv[1])
	visualize(data, 100000)
