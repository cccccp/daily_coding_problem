def longest_substring(s,k): #O(n) time/space complexity
    n=len(s)
    
    maxss=''
    distinct_characters=set()
    l=0 #or len(distinct_characters)
    
    ss=''
    begin=0
    end=-1
    
    while end<n-1:
        end+=1
        ch=s[end]
        
        ss+=ch
        if ch not in distinct_characters:
            l+=1
            distinct_characters.add(ch)
            
        if end-begin+1>len(maxss) and l<=k:
            maxss=ss
        
        if l>k:
            ss=ss[1:]
            
            distinct_characters.remove(s[begin])
            l-=1
            
            begin+=1
            
    return maxss
