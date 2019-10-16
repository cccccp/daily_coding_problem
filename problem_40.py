def lonesome(A,k=3): #O(n) time complexity/ O(1) space complexity if the entries of A are bounded
    l=0
    for a in A:
        l=max(l,int(log(a,k))+1)
   
    digits=[0]*l
    for a in A:
        q=a
        for i in range(l):
            r=q%k
            q=q//k
            digits[i]=(digits[i]+r)%k
       
    return sum(digits[i]*k**i for i in range(l))
