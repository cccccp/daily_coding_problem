#exponentiation rapide en anglais
def square_and_multiply(x,n):
	if n==0:
		return 1
	elif n==1:
		return x
	else:
		m=n//2
		y=square_and_multiply(x,m)
		if m%2==0:
			return y*y
		else:
			return y*y*x
