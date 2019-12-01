def numberinmultiplicationtable(X,n):
    count=0
    for i in range(1,min(n,X)+1):
        if X%i==0 and X//i<=n:
            count+=1
    return count
