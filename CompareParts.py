# -*- coding: utf-8 -*-

def getcolumn(filename, column_no, delimiter=",", header="True"):
	with open(filename, "r") as f:
		lines = f.readlines()

		if header:
			column_names = lines[0].split(delimiter)
			del lines[0]

		values = []
		for line in lines:
			values.append(line.split(delimiter)[column_no].strip())

		values = set(values)
		return values

filename = "c:\\users\\victor\\Downloads\\Odoo\\HKBOM_UTF8.txt"

values1 = getcolumn(filename, 0, delimiter="#")
values2 = getcolumn(filename, 2, delimiter="#")

values3 = getcolumn("allinone.txt", 1, delimiter="|")


# 比較母件跟料件編號的差別, 將結果輸出到檔案

# values = values1 - values2
values = values2 - values1

filename = "parts.txt"

f = open(filename, "w")

values = sorted(list(set(values)))
for value in values:
	f.write(value + "\n")

f.close()

# 看看是不是訂單上面所有的編號, BOM裡面都找的到

print len(values3 - values1)
print len(values3 - values1 - values2)
