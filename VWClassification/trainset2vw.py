import sys
import math

line = sys.stdin.readline()

for line in sys.stdin:

	splitted = line[0:-1].split("\t")
	label = "1" if splitted[0] == "1" else "-1"

	numericals = splitted[1:13]
	categoricals = splitted[14:]


	transed = label + " "

	#transed += "|l "
	
	for i in range(0, len(numericals)):
		if numericals[i] == "":
			continue
		#transed += "l" + str(i) + ":"
		transed += "|l" + str(i) + " "
		transed += "" if numericals[i] == "" else str(0 if numericals[i] == "0" else int(math.copysign( (math.log(math.fabs(int(numericals[i])))), int(numericals[i])) )   )
		#transed += (numericals[i])
		transed += " "


	transed += "|c "
	for i in range(0, len(categoricals)):
		#transed += "|c" + str(i)
		transed += " "
		transed += categoricals[i] + " "


	print(transed)

