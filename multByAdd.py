def multByAdd(a,b):
	if not b:
		return 0
	else: return a+multByAdd(a,b-1)

print multByAdd(100,100)