def isIncrease(number,last,isIt):
	if isIt:
		if number:
			newLast=number%10
			if last>=newLast:
				return isIncrease(number/10,last,True)
			else: return isIncrease(number/10,last,False)
		else: return isIt
	else: return False

number=1233487
print isIncrease(number/10,number%10,True)