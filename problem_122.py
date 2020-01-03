def maxsum(matrix):
	n=len(matrix)
	m=len(matrix[0])
	
	# maxsums[i][j] is the maximum sum on can get starting from (i,j) and ending at (n-1,m-1)
	maxsums=[[None]*m for _ in range(n)]
	
	# Definition of maxsums on the last row and column of the matrix
	maxsums[n-1][m-1]=matrix[n-1][m-1]
	for j in range(m-1,0,-1):
		maxsums[n-1][j-1]=maxsums[n-1][j]+matrix[n-1][j-1]
	for i in range(n-1,0,-1):
		maxsums[i-1][m-1]=maxsums[i][m-1]+matrix[i-1][m-1]
		
	# Use a closure to avoid useless calls of maxsum2
	def maxsum2(i,j):
		if maxsums[i][j] is None:
			val=matrix[i][j]+max(maxsum2(i+1,j),maxsum2(i,j+1))
			maxsums[i][j]=val
			return val
		else:
			return maxsums[i][j]
	
	return maxsum2(0,0)
