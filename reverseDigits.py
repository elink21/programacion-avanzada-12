def reverseDigits(number,n):
	if(number):
		return str(number%10)+(reverseDigits(number/10,n+1))
	else: return ""
print int(reverseDigits(12345,0))