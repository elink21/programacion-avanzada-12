def sumSquares(limit):
	if limit==0:
		return 0
	else : return limit**2+sumSquares(limit-1)


print sumSquares(4)