def reverseBetweenLimits( arr,l,r):
	if(l>r):
		return arr
	else:
		arr[l],arr[r]=arr[r],arr[l]
		return reverseBetweenLimits(arr,l+1,r-1)

a=list(range(10))
print reverseBetweenLimits(a,5,7)