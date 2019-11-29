def binomial(n,k):
    coeff=1
    for i in range(k):
        coeff*=n-i
        coeff//=i+1
    return coeff

def ways(N,M):
	return binomial(N-1+M-1,N-1)
