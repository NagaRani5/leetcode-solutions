class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=len(s1)
        b=len(s2)
        for i in range(b-a+1):
            c=s2[i:a+i]
            if sorted(c)==sorted(s1):
                return True
        return False
        