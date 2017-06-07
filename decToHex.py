
def decToHexOct(number, base):
	hexMap={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
	if number:
		if base==16:
			return str(hexMap[ number%16 ])+ str(decToHexOct(number/16,base))
		else: 
			if base==8:
				return str(hexMap[number%8])+ str(decToHexOct(number/8,base))
	else:
		return ""

print decToHexOct(753,16)[::-1]
	