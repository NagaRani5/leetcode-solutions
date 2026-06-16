class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        a=set()
        for i in range(len(s)):
            if s[i] not in d and t[i] not in a:
                d[s[i]]=t[i]
                a.add(t[i])
            elif s[i] in d and d[s[i]]!=t[i]:
                return False
            elif s[i] not in d and t[i] in a:
                return False
        return True
        

            
        
                



        