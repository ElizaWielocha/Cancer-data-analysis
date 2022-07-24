import pandas as pd
from pandas import DataFrame
from pathlib import Path
import os
import csv
import numpy as np

# create dicts for mutations, their counts and file names
mutations = dict()
file_names = dict()

# open file with repeated mutations, delete unnecessary columns, count mutations and add data to appropriate dictionaries
f = open("check.txt", "r")
for line in f:
	file = line.split('ID', 1)[1]
	file = file.split('.')[0]
	mutation = line.split(':', 1)[1]
	mutation = mutation.split("\t")[0:7]
	del mutation[2]
	del mutation[4]
	gene = mutation[-1]
	mutation = (' | ').join(mutation)

	if mutation in mutations:
		mutations[mutation] += 1
		file_names[mutation] += f', {file}'
	else:
		mutations[mutation] = 1
		file_names[mutation] = f'{file}'

f.close()

# Create table with mutations, how many and in which files
table = pd.DataFrame(columns= ["Chr", "Pozycja", "Ref", "Alt", "Gen", "liczba powtórzeń", "Numery próbek"])
j = 0
for key in mutations:
	chr = key.split('|')[0]
	pos = key.split('|')[1]
	ref = key.split('|')[2]
	alt = key.split('|')[3]
	gen = key.split('|')[4]
	table.loc[j] = [chr, pos, ref, alt, gen, mutations[key], file_names[key]]
	j += 1

table.to_csv("table_of_repeated_mutations.csv", sep=",", index=False)

