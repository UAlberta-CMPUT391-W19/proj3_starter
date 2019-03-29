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

else:

	if "error" in " ".join(lines).lower():
		print "====> SUCCESS 1: output is formatted correctly"
		exit(0)

	if len(lines) == 1:

		try:
			t = lines[0].split('\t')
			areaId, distance = t[0], float(t[1])	
			print "====> SUCCESS 2: output is formatted correctly"
			exit(0)
		except Exception as e:
			print "====> ERROR 1: output does not meet specifications"
			exit(1)

	print "====> ERROR 2: output does not meet specifications"
	exit(1)
