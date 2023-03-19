import os
from datetime import date

today = date.today()

dir_list = os.listdir("./")

maxnum = 0

l = []


for f in dir_list:
	if f[:2] == 'HW':
		l.append(int(f[2:4]))

maxnum = max(l)+1

with open(f'HW{maxnum:02d}_PeterSaburov.py', 'w') as file:
	file.write(f'\"\"\"\nPeter Saburov\nCS 100 2023S Section 012\nHW {maxnum:02d}, {today.strftime("%b %d, %Y")}\n\"\"\"')