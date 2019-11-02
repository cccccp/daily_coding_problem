def splitting(text,k):
    strings=text.split()
    
    tab=[]
    
    start=0
    end=0        
        
    while end<len(strings):
        word=""
        while end<len(strings) and len(word)+len(strings[end])<=k:
            word+=strings[end]+" "
            end+=1
        tab.append(word[:-1])
        start=end
            
    return tab
