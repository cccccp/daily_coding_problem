def longestpalindrome(char): # Manacher's algorithm: O(n) time/space complexity (since right is incremented for each value of i)
    # To avoid problems with even sized longest palindroms
    s="^#"+"#".join(char)+"#$"
    n=len(s)
    
    # definition of two auxilary parameters (right is the uppest index of the previous longest palindroms; center is the corresponding position)
    cen=0
    right=0
    
    # array of the lengths of the longest palindroms centered at any position
    p=[0]*n
    
    pal=""
    length=0
    
    for i in range(1,n-1):
        
        # definition of a lower bound for the palindrom centered at i
        
        # Since (obviously) i+ min(p[mir],right-i)<=right, one has mir-min(p[mir],right-i)>=left (the symmetric of right, w.r.t. cen) 
        # and consequently the sub-palindrom centered in mir of radius min(p[mir],right-i)(<=p[mir]) is included in the first-half of the longest palindrom centered in cen.
        # Hence p[i] >=min(p[mir],right-i) (the symmetric of any palindrom centered in mir, w.r.t. cen, is also a palindrom).
        
        mir=cen-(i-cen)
        p[i]=max(0,min(p[mir],right-i))
        
        # determination of the length of the longest palindrom centered at i
        while p[i]+1<=min(i,n-1-i) and s[i-p[i]-1]==s[i+p[i]+1]:
            p[i]+=1
        
        if p[i]>length:
            length=p[i]
            pal=s[i-p[i]+1:i+p[i]+1:2] # pal is necessary of the form #a1#a2...#an# where a1...an is a palindromic substring of 
            
        # new definition of the auxilary indexes
        if i+p[i]>right:
            right=i+p[i]
            cen=i
    
    return pal
