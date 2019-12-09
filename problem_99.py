def largestconsecutive(arr): # Runs in O(max(A)-min(A))
    m,M=min(arr),max(arr)
	
    s=set(arr)
    
	currentm,currentM=m,M
    current=[]
    length=0
    currentMax,lengthMax=current,length
   
    while currentm<=M:
        while currentM in s:
            current.append(currentM)
            length+=1
            currentM+=1
            if length>lengthMax:
                lengthMax=length
                currentMax=current
        current=[]
        length=0
        if currentM+1<=M:
            currentm=currentM+1
            while currentm not in s:
                currentm+=1
            currentM=currentm
        else:
            break
    return currentMax,lengthMax
