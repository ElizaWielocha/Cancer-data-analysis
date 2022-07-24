
# comparing noncoding somatic mutations from 7 samples after treatment with 162 samples from TCGA 

# open file containing all somatic mutations 
merged_mutations = open("merged_somatic.txt", encoding="utf-8")


# create lists and add to them needed data 
AML_mutations = []
for line in merged_mutations:
	line = line.replace("'", "").replace("\n", "").replace(" ", "").replace("(", "").replace(")", "").split(',')
	AML_mutations.append((
		line[0], #chr
		line[1], #pos
		line[2], #ref
		line[3]  #alt
	))


# open file containg all somatic mutations in noncoding regions from TCGA data 
TCGA_merged_mutations = open("TCGA_LAML_MuTect2.somatic_annotation_merged_v2.vcf")
for i in range(0,77):
	next(TCGA_merged_mutations)


# create lists and add to them needed data 
AML_TCGA_mutations = []
for line in TCGA_merged_mutations:
	line = line.split('\t')
	AML_TCGA_mutations.append((
		line[0].replace('chr', ''), #chr
		line[1], #pos
		line[3], #ref
		line[4]  #alt
	))

# compare rows with each other, if they are the same, write to output file
with open("tcga_merged_somatic_mutations_comparing.txt", "w") as f:
	for AML_row in AML_mutations:
		same = False
		for AML_TCGA_row in AML_TCGA_mutations:
			if AML_row == AML_TCGA_row:
				same = True

		if same == True:
			add = str(AML_row)
			add = add.lstrip("(")
			add = add.rstrip(")")
			f.write(add)
			f.write('\n')
			print(add)


# -----------------------------------------------------------------------------------------
# comparing all noncoding mutations from 38 samples with 162 samples from TCGA

# open file containing all noncoding mutations
merged_mutations = open("merged_all_noncoding.tsv", encoding="utf-8")
next(merged_mutations)


# create lists and add to them needed data 
AML_mutations = []
for line in merged_mutations:
	line = line.split('\t')
	AML_mutations.append((
		line[0], #chr
		line[1], #pos
		line[3], #ref
		line[4]  #alt
	))


# open file containg all somatic mutations in noncoding regions from TCGA data 
TCGA_merged_mutations = open("TCGA_LAML_MuTect2.somatic_annotation_merged_v2.vcf")
for i in range(0,77):
	next(TCGA_merged_mutations)


# create lists and add to them needed data 
AML_TCGA_mutations = []
for line in TCGA_merged_mutations:
	line = line.split('\t')
	AML_TCGA_mutations.append((
		line[0].replace('chr', ''), #chr
		line[1], #pos
		line[3], #ref
		line[4]  #alt
	))


# compare rows with each other, if they are the same, write to output file
with open("tcga_merged_all_mutations_comparing.txt", "w") as f:
	for AML_row in AML_mutations:
		same = False
		for AML_TCGA_row in AML_TCGA_mutations:
			if AML_row == AML_TCGA_row:
				same = True

		if same == True:
			add = str(AML_row)
			add = add.lstrip("(")
			add = add.rstrip(")")
			f.write(add)
			f.write('\n')
			print(add)
