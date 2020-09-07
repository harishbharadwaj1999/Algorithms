import collections as c
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d=c.defaultdict(int)
        for t in matrix:
            j=t[0]
            k=[]
            for i in range(len(t)):
                if j==t[i]:
                    continue
                else:
                    k.append(i)
                    j=t[i]
            d[tuple(k)]+=1
        return max(list(d.values()))
