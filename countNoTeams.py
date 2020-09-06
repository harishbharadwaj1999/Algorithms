def numTeams(self, rating: List[int]) -> int:
        c=0
        for i in range(len(rating)):
            ll=lu=rl=ru=0
            if i>0:
                for j in range(i-1,-1,-1):
                    if rating[j]<rating[i]:
                        ll+=1
                    elif rating[j]>rating[i]:
                        lu+=1
            if i<len(rating)-1:
                for j in range(i+1,len(rating)):
                    if rating[i]>rating[j]:
                        rl+=1
                    elif rating[j]>rating[i]:
                        ru+=1
            c+=lu*rl+ll*ru
        return c
