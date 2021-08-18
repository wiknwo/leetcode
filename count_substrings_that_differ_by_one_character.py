def countSubstrings(self, s: str, t: str) -> int:
	"""
	Given two strings s and t, find the number of ways 
	you can choose a non-empty substring of s and replace 
	a single character by a different character such that 
	the resulting substring is a substring of t. In other 
	words, find the number of substrings in s that differ 
	from some substring in t by exactly one character.
	"""
	Ns, Nt, N, total, = len(s), len(t), len(s), 0
	
	for i in range(len(s)):
		for j in range(len(t)):
			delta = 0 # Number of different characters
			for k in range(N):
				# We exit if we go out of bounds
				if i + k >= Ns or j + k >= Nt:
					break
				if s[i + k] != t[j + k]:
					delta += 1
				if delta == 1:
					total += 1
	return total