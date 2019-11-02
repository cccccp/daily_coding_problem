def rgb(A):
	r,g,b=0,0,0
	for a in A:
		if a=='R':
			r+=1
		elif a=='G':
			g+=1
		else:
			b+=1
	return ['R']*r+['G']*g+['B']*b

# In place version:
def rgb(A):
	n=len(A)
	r,g,b=0,0,0
	for a in A:
		if a=='R':
			r+=1
		elif a=='G':
			g+=1
		else:
			b+=1
	for i in range(n):
		if i<r:
			A[i]='R'
		elif i<r+g:
			A[i]='G'
		else:
			A[i]='B'
	return A
