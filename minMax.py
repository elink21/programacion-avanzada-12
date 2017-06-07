def minMax(arr,n,minim,maxim):
	if n<len(arr):
		if arr[n]<minim: minim=arr[n]
		if arr[n]>maxim: maxim=arr[n]
		return minMax(arr,n+1,minim,maxim)
	else: return [minim,maxim]


print minMax([1,2,3,4,5],0,1e9,0)