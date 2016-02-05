# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 3:
	print "Usage: python getcolumn.py <input filename> <column #>"
	sys.exit()

file1 = open(sys.argv[1], "r")

column_no = int(sys.argv[2])

lines = file1.readlines()

column_names = lines[0].split("#")

"""
# 將欄位名稱輸出到文字檔

tempfile = open("column_names.txt", "w")

for i in range(len(column_names)):
	column_name = "(%s) %s\n" % (i, column_names[i])
	tempfile.write(column_name)

tempfile.close()
"""

del lines[0]

# 將欄位內容輸出到以欄位名稱做為檔名的檔案

values = []
for line in lines:
	values.append(line.split("#")[column_no].strip())

filename = "%s - %s.txt" % (column_names[column_no], column_no)

file2 = open(filename.decode("utf-8"), "w")

values = sorted(list(set(values)))
for value in values:
	file2.write(value + "\n")

file2.close()
file1.close()
