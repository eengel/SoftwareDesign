a=4.5
b=3
c=9
n=3


def check_fermat(a,b,c,n):
    if n > 2 and (a**n + b**n) == c**n:
        print 'Holy smokes, Fermat was wrong!'
    else:
        print "No, that doesn't work."
        
check_fermat(a,b,c,n)
        
def integer_check_fermat(a,b,c,n):
    int(a)
    int(b)
    int(c)
    int(n)
    check_fermat(a,b,c,n)
    
integer_check_fermat(a,b,c,n)