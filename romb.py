def romb(i,j,k):
	if i<j:
		return " "*(  (k)-i )+"* "*i+"\n"+romb(i+1,j,k)
	else:
		if j>0:
			return " "*(  (k)-j )+"* "*j+"\n"+romb(i,j-1,k)
		else:
			return ""
n=10
print romb(0,n,n)