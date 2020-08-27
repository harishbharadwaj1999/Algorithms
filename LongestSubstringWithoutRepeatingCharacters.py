def lengthOfLongestSubstring(self, s: str) -> int:
        queue=[]
        c=0
        m=0
        for i in range(len(s)):
            if s[i] not in queue:
                queue.append(s[i])
                c+=1
            else:
                c=len(queue)
                while(queue[0]!=s[i]):
                    if len(queue)>0:
                        queue.pop(0)
                if len(queue)>0:
                    queue.pop(0)
                queue.append(s[i])
                if m<c:
                    m=c
        if len(queue)>m:
            m=len(queue)
        return m
