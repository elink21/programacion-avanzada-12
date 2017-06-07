def squareRoot(x,a,eps,):
	if abs(a**2-x)<=eps:
		return a
	else:
		a=float((a**2+x)/(2*a))
		return squareRoot(x,a,eps)
print squareRoot(20,20,.01)