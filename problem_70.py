perfectlist=[]
    for a in range(1,10):
        b=10-a
        perfectlist.append(10*a+b)
    for a in range(1,10):
        for b in range(11-a):
            c=10-(b+c)
            perfectlist.append(100*a+10*b+c)
    for a in range(1,10):
        for b in range(11-a):
            for c in range(11-a-b):
                d=10-(a+b+c)
                perfectlist.append(1000*a+100*b+10*c+d)
    for a in range(1,10):
        for b in range(11-a):
            for c in range(11-a-b):
                d=10-(a+b+c)
                perfectlist.append(1000*a+100*b+10*c+d)
    for a in range(1,10):
        for b in range(11-a):
            for c in range(11-a-b):
                for d in range(11-a-b-c):
                    e=10-(a+b+c+d)
                    perfectlist.append(10000*a+1000*b+100*c+10*d+e)
    for a in range(1,10):
        for b in range(11-a):
            for c in range(11-a-b):
                for d in range(11-a-b-c):
                    for e in range(11-a-b-c-d):
                        f=10-(a+b+c+d+e)
                        perfectlist.append(10**5*a+10**4*b+10**3*c+10**2*d+10*e+f)
                        


def perfect(n):
    return perfectlist[n+1]
