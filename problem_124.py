# One has, for any n>=2, e(n)=1+\sum_{k=0}^n binom(n,k)/2^n e(k) and e(1)=e(0)=0

dic={0:0,1:0}

def binom(n,k):
  c=1
  for i in range(k):
    c=c*(n-i)//(i+1)
  return c

def expectation(n):
  if n in dic:
    return dic[n]
  else:
    p=2**n
    val=p/(p-1)+sum(binom(n,k)*expectation(k) for k in range(2,n))/(p-1)
    dic[n]=val
    return val
