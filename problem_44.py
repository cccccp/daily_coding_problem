def inversions_merge(A1,A2): # auxilary function to merge 2 sorted lists and count the number of remaining inversions (O(max(n1,n2)) time complexity, O(n1+n2) space complexity)         
    n1, n2=len(A1), len(A2) 
    B=[]
    
    inv = 0
    # current A1-index for comparison
    i = 0          

    for j in range(n2):
        while i<n1 and A1[i] < A2[j]:
            B.append(A1[i])  
            i += 1

        if i <n1:
            inv += n1-i
        
        B.append(A2[j])

    # append the remaining elements of A1 to B (if any)
    while i < n1:
            B.append(A1[i])
            i+=1

    return inv, B

# @trace
def inversions(A): # O(nlog(n)) time/space complexity
    n=len(A)
    if n<2:
        return 0,A
    inv1, A1 = inversions(A[:n//2])
    inv2, A2 = inversions(A[n//2:])
    inv, A = inversions_merge(A1, A2) 
    return inv+inv1+inv2, A 
