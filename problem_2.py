#With division
def products_without_element(array):
    P=1
    for x in array:
        P*=x
    return [P//x for x in array]
        
#Without division
def products_without_element2(array):
    n=len(array)
    products_right=[1]*n
    products_left=[1]*n
    
    for i in range(1,n):
        products_left[i]=products_left[i-1]*array[i-1]

    for i in range(n-2,-1,-1):
        products_right[i]=products_right[i+1]*array[i+1]        
        
    return [products_left[i]*products_right[i] for i in range(n)]
