def max_contiguous_sum(A):#O(n) time complexity/ O(1) space complexity
	n=len(A)
	s=0
	m=float('inf')
	M=float('-inf')
	for i in range(n):
		m=min(s,m)
		s+=A[i]
		M=max(M,s-m)
		
	return M
