def powRecursive(x,y):
	if y==0:
		return 1
	elif y>0:
		return x * powRecursive(x,y-1)
	elif y<0:
		return 1 / powRecursive(x,-1*y)

print powRecursive(2,4)