class Solution:
    def reverse(self, x: int) -> int:
        r=0
        c=0
        if x<0:
            x=-x
            c=1
        while x>0:
            d=x%10
            x=x//10
            r=r*10+d
        if c==1:
            r=-r
        if r<-2**31 or r>2**31-1:
            r=0
        return r
            
        
        


        