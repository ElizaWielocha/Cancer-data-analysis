''' 
Script has been used 2 times: 
1) for a file tcga_merged_somatic_mutations_comparing.txt and the output file was tcga_merged_somatic_counts.txt
2) for a file tcga_merged_all_mutations_comparing.txt and the output file was tcga_merged_all_counts.txt
'''

compared_mutations = open("tcga_merged_all_mutations_comparing.txt", encoding="utf-8")
mutations_counts = dict()

for line in compared_mutations:
	if line not in mutations_counts:
		mutations_counts[line] = 1
	else:
		mutations_counts[line] += 1

mutations_counts = sorted(mutations_counts.items(), key=lambda x: x[1], reverse=True)
mutations_counts = dict(mutations_counts)

with open("tcga_merged_all_counts.txt", "w") as f:
	for key in mutations_counts:
		f.write(f'{mutations_counts[key]}	{key}')
