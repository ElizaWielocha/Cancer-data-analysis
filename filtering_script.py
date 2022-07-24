import pandas as pd
from pandas import DataFrame
from tkinter import filedialog
from pathlib import Path
import os

# Script processed one file at a time because it contained a lot of data

# list of non_coding_variant
nonCodingWariants = [
"3_prime_UTR_variant",
"5_prime_UTR_variant",
"TFBS_ablation",
"TFBS_ablation",
"downstream_gene_variant",
"intragenic_variant",
"intergenic_variant",
"intron_variant",
"mature_miRNA_variant",
"mature_miRNA_variant",
"non_coding_transcript_variant",
"regulatory_region_variant",
"splice_acceptor_variant",
"splice_donor_variant",
"splice_region_variant",
"upstream_gene_variant"
]

# import data from sample
import_file_path = filedialog.askopenfilename()
file_name = Path(import_file_path).name.split('.')[0]


# create dataframe from sample 
sample = pd.read_csv(import_file_path, sep='\t', dtype='str', encoding='latin-1') 


# print dataframe length before filtering 
print("Length of dataframe before filtering: ", len(sample.index))
before = len(sample.index)


# change needed columns to ints
sample = sample.astype({f"{file_name}.COV" : int, f"{file_name}.RO" : int, f"{file_name}.AO" : int}) 


# delete duplicates
sample = sample.drop_duplicates(
	subset = ["CHR", "START", "END"],
	keep = 'last'
)


# filter after COV, RO and AO
indexes_COV_RO_AO = sample[ (sample[f"{file_name}.AO"] < 10) | (sample[f"{file_name}.RO"] < 10) | (sample[f"{file_name}.COV"] < 20) ].index 
sample.drop(indexes_COV_RO_AO, inplace=True) 


# create 2 dataframes - first for noncoding and second for coding 
noncodingSample = sample.copy()
codingSample = sample.copy()

indexes_EFFECT = list()


# fill indexes_EFFECT list with indexes of coding variants
for index,row in sample.iterrows():
	if '&' in row["EFFECT"]:
		for i in row["EFFECT"].split('&'):
			if i not in nonCodingWariants:
				indexes_EFFECT.append(index) 
	else:
		if row["EFFECT"] not in nonCodingWariants:
			indexes_EFFECT.append(index)


# delete from datafame all coding indexes of variants -> dataframe contains only noncoding variants
noncodingSample.drop(index=indexes_EFFECT, inplace=True) 

# delete from datafame all noncoding indexes of variants -> dataframe contains only coding variants
for i in sample.index:
	if i not in indexes_EFFECT:
		codingSample.drop(index=i, inplace=True)


# save dataframes to output files
noncodingSample.to_csv(f"noncoding_{file_name}.tsv", sep="\t", index=False)
print(f"New filtered sample was saved as: noncoding_{file_name}.tsv")

codingSample.to_csv(f"coding_{file_name}.tsv", sep="\t", index=False)
print(f"New filtered sample was saved as: coding_{file_name}.tsv")

# print lengths of dataframes
print("Length of non coding dataframe after filtering: ", len(noncodingSample.index))
print("Length of coding dataframe after filtering:", len(codingSample.index))

