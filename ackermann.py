def ackermann(m,n):
	if not m:
		return n+1
	elif n==0:
		return ackermann(m-1,1)
	else:
		return ackermann(m-1,ackermann(m,n-1))

print ackermann(4,3)