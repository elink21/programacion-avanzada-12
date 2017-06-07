def sumArray(arr,n):
	if n<len(arr):
		return arr[n]+sumArray(arr,n+1)
	else: return 0

print sumArray([1,2,3,4,5,6],0)
