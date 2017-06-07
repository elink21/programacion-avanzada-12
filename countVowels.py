def countVowels(string, n):
	if n<len(string):
		if string[n] in "aeiou":
			return 1+countVowels(string,n+1)
		else: return countVowels(string,n+1)
	else: return 0


print countVowels("murcielago",0)