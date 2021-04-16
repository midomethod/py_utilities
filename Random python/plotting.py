#!/usr/bin/env python3

import sys, os, re
import matplotlib.pyplot as plt
import pandas as pd

os.system('make clean; make; mkdir figures;')

mapping = {
	's': 'arcSin',
	'c': 'arcCos',
	't': 'arcTan',
	'l': 'Log'
}

for func in ['s', 'c', 't', 'l']:

	for mode in ['test', 'test-bin']:
		os.system(f'./mathlib-{mode} -{func} > tmp1.txt')

		with open('tmp1.txt', 'r') as f1:
			in_ln_lst 	= f1.readlines()
			del in_ln_lst[1]
			out_ln_lst	= [re.sub(r' +', '\t', line) for line in in_ln_lst]

			with open('tmp2.txt', 'w') as f2:
				f2.writelines(out_ln_lst)

		df = pd.read_csv('tmp2.txt', delimiter="\t")
		ax = plt.gca()
		df.plot(kind='line',x='x', y=mapping[func], color='red', ax=ax)
		df.plot(kind='line',x='x', y='Library', color='blue', ax=ax)
		df.plot(kind='line',x='x', y='Difference', color='purple', ax=ax)

		plt.savefig(f'figures/figure-{func}-{mode}.png')
		plt.clf()

os.system('rm *.txt; make clean;')
