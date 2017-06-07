def seqSearch(arr,element,n):
	if n<len(arr):
		if arr[n]==element:
			return [n]+ seqSearch(arr,element,n+1)
		else: return seqSearch(arr,element,n+1)
	else:
		return []

arr=[1,2,3,4,5,5,5,6,7,8,9]
elem=5

print seqSearch(arr,elem,0)