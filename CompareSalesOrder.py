# -*- coding: utf-8 -*-

# 檢查重複的訂單編號

fin = open("allinone.txt", "r")
fout = open("result.txt","w")
lines = fin.readlines()
print len(lines)
so_numbers = []
count = len(lines)
for i in range(count):
	so_number = lines[i].split('|')[0]
	firsttime = True
	n = 1
	if so_number in so_numbers:
		continue
	else:
		so_numbers.append(so_number)
		for j in range(i+1,count):
			if lines[j].startswith(so_number):
				if firsttime:
					fout.write(lines[i])
					firstime = False
				fout.write(lines[j])
				n += 1
	if n > 1:
		print so_number, n

fout.close()
fin.close()