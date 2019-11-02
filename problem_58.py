def rotations(A):  # returns the index in A of the starting value of the unrotated version of A 
    a,b = 0,len(A)-1
    m=(a+b)//2
    
    while A[m] <= A[m+1]:
        if A[m] > A[b]:
            a = m
        else:
            b = m
        m = (a+b)//2
        
    return m+1


def search(A,x):
    n=len(A)
    start=rotations(A)
    end=rotations(A)-1 +n
    
    mid= (start+end)//2
    
    while start!=end:
        if (A[start%n] - x)*(A[mid%n] - x)>=0:
            start = mid
        else:
            end =mid
        mid= (start+end)//2
        
        if A[mid%n]==x:
            return mid%n
        
    return None  
