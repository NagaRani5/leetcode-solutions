class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        g.sort()
        s.sort()
        j=0
        for i in g:
            while j<len(s) and s[j]<i:
                j+=1
            if j<len(s):
                count+=1
                j+=1
        return count
            
        