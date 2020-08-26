def neg(ch):
    if ch=='w':
        return 'b'
    else:
        return 'w'
def chkAdj(k):
    for i in range(len(k)-1):
        if k[i]==k[i+1]:
            return False
    return True
def chkBox(t):
    for i in range(len(t)+1):
        k=t[i:]+t[:i]
        if chkAdj(k):
            return True
    return False
def minSum(x):
    c=0
    if chkBox(x):
        return c
    h=x
    for i in range(len(x)-1):
        if x[i]==x[i+1]:
            c+=1
            h[i+1]=neg(x[i+1])
            x=h
            if chkBox(x):
                return c
