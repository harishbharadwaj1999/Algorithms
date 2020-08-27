class Solution:
    def convert(self, s: str, numRows: int) -> str:
        z=2*(numRows-1)
        t=[]
        if len(s)<1:
            return ""
        if z==0 or len(s)<=2:
            return s
        for i in range(numRows):
            k=i*2
            j=i
            if i<len(s):
                t.append(s[i])
            while(j<len(s)):
                k=abs(z-k)
                if k==0:
                    k=z
                if j+k<len(s):
                    t.append(s[j+k])
                j+=k
        return ''.join(t)
