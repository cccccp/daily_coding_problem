def pow(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        y=pow(x,n//2)
        if n%2==0:
            return y*y
        else:
            return x*y*y
        
# Remark: a non-recursive algorithm uses the binary expansion of n
def pow(x,n):
    y=x
    p=1
    
    while n>0:
        r=n%2
        n=n//2
        
        if r!=0:
            p=y*p
        
        y*=y

    return p
