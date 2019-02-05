#! /usr/bin/python3.5

# combine two set of characters to generate two files:
# - a complete dictionary, even if some char forms are the same
# - a dictionary containing only char pairs with different forms

# input: two text files of the same length, with one character on each line. The first
# file should contain the original character forms, the second file should contain the
# converted character forms in the same positions as in the first file
#   python3 compare.py original_forms.txt converted_forms.txt

import sys

delimiter = ','

data_1 = []
data_2 = []
diff_char_1 = []
diff_char_2 = []
#diff_index = []

with open(sys.argv[1], 'r') as file:
	data_1 = file.read().splitlines()
	file.close()

with open(sys.argv[2], 'r') as file:
	data_2 = file.read().splitlines()
	file.close()

if len(data_1) == len(data_2):
	for i in range(len(data_1)):
		if (data_1[i] != data_2[i]):
			diff_char_1.append(data_1[i])
			diff_char_2.append(data_2[i])
			#diff_index.append(i)

	with open(sys.argv[3], 'w') as out_file:
		for i in range(len(data_1)):
			out_file.write("%s%s%s\n" % (data_1[i],delimiter,data_2[i]))
		out_file.close()

	with open(sys.argv[4], 'w') as diff_file:
		for i in range(len(diff_char_1)):
			diff_file.write("%s%s%s\n" % (diff_char_1[i],delimiter,diff_char_2[i]))
		diff_file.close()
else:
	print("Error: files do not have the same length")
