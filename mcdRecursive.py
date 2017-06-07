def mcdRecursive(x,y):
	if y==0:
		return x
	else: return mcdRecursive(x,y%x)

print mcdRecursive(3,6)