# -*- coding: utf-8 -*-

# 讀取所有訂單的 txt 檔
from os import listdir
from os.path import isfile, join

company_code = "P103"
mypath = "C:\\Users\\victor\\Downloads\\SO"

filenames = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f)) and f.startswith(company_code) and f.endswith('.txt')]

filenames.sort()

# 將所有檔案併成一個檔

outputfilename = "allinone.txt"

out = open(outputfilename, "w")

if filenames:
	for filename in filenames:
		with open(filename) as f:
			print filename
			lines = f.readlines()
			print len(lines)
			#for line in lines:
			#	print line.decode('big5').split('|')[23]
			for line in lines:
				out.write(line.decode('big5').encode('utf-8'))

out.close()
