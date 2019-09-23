def minimal_positive(array):
    d=dict()
    for x in array:
        d[x]=0
    
    i=1
    while True:
        try:
            d[i]
        except KeyError:
            return i
        i+=1
