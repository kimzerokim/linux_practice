multiple = 1;
resultText = '';

for i in range(1,10) :
	for i in range(1,10) :
		result = i * multiple;
		if (i == 1) :
			resultText += str(result) + '  ';
		elif (result < 10) : 
			resultText += ' ' + str(result) + '  ';
		else :
			resultText += str(result) + '  ';
	print resultText;
	resultText = '';
	multiple += 1;
	result = 0;
	
print "Done!";