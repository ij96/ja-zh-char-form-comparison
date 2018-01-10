#! /usr/bin/python3.5

# list the difference between two files, one containing simplified Chinese
# while the other traditional

import sys

data_s = []
data_t = []
diff_char_s = []
diff_char_t = []
diff_index = []

with open(sys.argv[1], 'r') as file:
	data_s = list(file.read())

with open(sys.argv[2], 'r') as file:
	data_t = list(file.read())

for i in range(len(data_s)):
	if (data_s[i] != data_t[i]):
		#print(data_s[i],data_t[i],i)
		diff_char_s.append(data_s[i])
		diff_char_t.append(data_t[i])
		diff_index.append(i)
	else:
		counter = 0

with open(sys.argv[3], 'w') as out_file:
	for i in range(len(diff_char_s)):
		out_file.write("%s %s\n" % (diff_char_s[i],diff_char_t[i]))