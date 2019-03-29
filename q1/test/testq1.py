'''
Checks the output of the solution for Q2
'''

import sys
import subprocess

print "testing Q1"

x = 20
y = 10

output=subprocess.check_output(["./bin/solution.out", "./test/testq1.db", str(x), str(y)])
lines = output.strip().split('\n')

if len(lines) == 0:
	print "====> ERROR: there is no output"
	exit(1)

if len(lines) == 1:
	try:
		t = lines[0].split('\t')
		areaId, distance = t[0], float(t[1])	
	except:
		print "====> ERROR: output does not meet specifications"
		exit(1)
	print "====> SUCCESS: output is formatted correctly"
else:
	if "ERROR" in lines[0]:
		print "====> SUCCESS: output is formatted correctly"
		exit(0)
	else:
		print "====> ERROR: output does not meet specifications"
		exit(1)
