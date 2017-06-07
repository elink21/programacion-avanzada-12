def concavePrint(i,j,k):
	if i>0:
		return "*"*i+"\n"+concavePrint(i-1,j,k)
	else:
		if j<=k:
			return "*"*j+"\n"+concavePrint(i,j+1,k)
		else:
			return "" 
n=10
print concavePrint(n,0,n)