class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r=0
        l=0
        x=set()
        for i in range(len(s)):
            while s[i] in x:
                x.remove(s[l])
                l+=1
            x.add(s[i])
            r=max(r,i-l+1)
        return r
        


        
