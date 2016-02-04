# -*- coding: utf-8 -*-

# 讀取所有訂單的 txt 檔
from os import listdir
from os.path import isfile, join

company_code = "P103"
mypath = "C:\\Users\\victor\\Downloads\\SO"

filenames = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f)) and f.startswith(company_code) and f.endswith('.txt')]

filenames.sort()

print filenames

# 檢查所有檔案的訂單編號是否重複
if filenames:
	for filename in filenames:
		with open(filename) as f:
			print filename
			lines = f.readlines()
			print len(lines)
			lines = [line.decode('big5').split('|')[0] for line in lines]
			lines = set(lines)
			print len(lines)
