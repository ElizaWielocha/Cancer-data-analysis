# Script compares one file containing data before treatment with a file containing data after treatment for the same patient


# open files cotaing data before and after treatment 
before_treatment = open("data_before.tsv", encoding="utf-8")
after_treatment = open("data_after.csv", encoding="utf-8") # before opening changed file format from .vcf to .csv

'''
before treatment | after treatment
    ID012               ID018
    ID016               ID020
    ID026               ID027
    ID041               ID071
    ID049               ID065
    ID069               ID075
    ID087               ID099
'''

# create a list conating only needed info about variants
before_treatment_data = []
next(before_treatment) # Skip line with headers
for index, each in enumerate(before_treatment):
  if each:
    splitted = each.split()
    before_treatment_data.append((
      splitted[0], # CHR
      splitted[1], # START
      splitted[3], # REF
      splitted[4], # ALT
    ))

# create a list conating only needed info about variants
after_treatment_data = []
next(after_treatment)
for each in after_treatment:
  if each:
    splitted = each.split(';')
    after_treatment_data.append((
        splitted[0], # CHR
        splitted[1], # POS
        splitted[3], # REF
        splitted[4], # ALT
    ))

# comparing every variant from data before treatment with every variant from data after treatment
with open('compared_data_before_and_data_after.txt', 'w') as f:
  count = 0
  same = False
  for before_treatment_row in before_treatment_data:
    same = False
    for after_treatment_row in after_treatment_data:
      if before_treatment_row == after_treatment_row:
        same = True
  
    if same == False:
      count += 1
      f.write(str(before_treatment_row))
      f.write('\n')

print("Liczba mutacji somatycznych: ", count)
