# Reject method: we first simulate a uniform draw on a set of 5^2(>7) elements  

def rand7():
    a,b=0,0
    while not(a==1 or (a==2 and b<=2)):
        a,b=rand5(),rand5()
    if a==1:
        return b
    else:
        return b+5
