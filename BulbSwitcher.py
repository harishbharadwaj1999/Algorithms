def minFlips(self, target: str) -> int:
        c=1
        target=target.lstrip('0')
        if len(target)==0:
            return 0
        j=target[0]
        for i in range(1,len(target)):
            if target[i]!=j:
                c+=1
                j=target[i]
            else:
                continue
        return c
