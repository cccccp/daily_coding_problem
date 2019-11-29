#Von Neumann's trick
def toss_unbiased():
    x0=0
    x1=0
    while x0+x1==0:
        x0=toss_biased()
        x1=toss_biased()
    if x0!=0:
        return 0
    else: 
        return 1
