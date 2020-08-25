#Sieve of eratosthenes
def soe(n):
        t=[]
        for i in range(n+1):
            t.append(1)
        t[0]=0
        t[1]=0
        for i in range(len(t)):
            if t[i]==1:
                j=i
                while j<=n:
                    j+=i
                    if j<=n:
                        t[j]=0
        return sum(t)
#soe returns number of prime numbers present upto n
