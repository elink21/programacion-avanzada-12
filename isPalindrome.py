def isPalindrome(word,l,r,equal):
	if equal:
		if l==r:
			return equal
		else:
			if word[l]==word[r]:
				return isPalindrome(word,l+1,r-1,True)
			else: return isPalindrome ( word,l+1,r-1,False)
	else: return False


w="emadame"
print isPalindrome(w,0,len(w)-1,True)