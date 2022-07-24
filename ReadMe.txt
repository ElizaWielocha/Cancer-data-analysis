
This repository contains 5 scripts and 1 command line used to analyze exome sequencing (NGS) data from AML patients. 
filtering_script.py -> filters the sample data (removes variants with too low coverage below 20 and repetitive variants at one sample level) 
and divides the variants into those in non-coding fragments and those in coding fragments. It creates two result files. 

repeated_mutations.py -> loads a file containing mutations that repeat in individual samples at least 2 times (it was created thanks to the linux command line) 
and creates a table from them containing information about chromosome number, position, reference and alternative allele, gene, number of times the variant 
repeats and in which samples it repeats.

somatic_mutations.py -> script compares mutations from the sample before treating the patient with mutations from the sample after treating the patient. 
If the variant is present in the sample before treatment, but no longer in the sample after - such mutation is somatic. 
The script creates a result file with somatic mutations in the given sample.

tcga_data_comparing.py -> The script compares data from patients obtained in favor of the analysis with data from the TCGA database. 
The TCGA data contained only somatic mutations in non-coding regions. 
The script compared the pre-treatment data and the post-treatment data with the data from the TCGA database.

counting_mutations.py -> This script only sorts and arranges the data from the result files created from the tcga_data_comparing.py script. 
