try:
    t=int(input())
    for i in range(t):
        n=int(input())
        l=[int(i) for i in input().split()]
        d={}
        p=[]
        for i in l:
            if d.get(i,None)==None:
                d[i]=1
                p.append(i)
            else:
                d[i]+=1
        for i in range(len(p)):
            p[i]=d[p[i]]
        p.sort()
        m=0
        c=1
        z=-1
        i=0
        for i in range(len(p)-1):
            if p[i]==p[i+1]:
                c+=1
            else:
                if c>m:
                    m=c
                    z=p[i]
                c=1
        if c>m:
            m=c
            z=p[i]
        print(z)
except:
    pass
