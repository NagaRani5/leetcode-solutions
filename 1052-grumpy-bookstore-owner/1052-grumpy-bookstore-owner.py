class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        a=len(customers)
        s=0
        r=[]
        for i in range(a):
            if grumpy[i]==0:
                s=s+customers[i]
                r.append(0)
            else:
                r.append(customers[i])
        d=[]
        for i in range(len(r)-minutes+1):
            b=r[i:minutes+i]
            c=sum(b)
            d.append(c)
        x=max(d)
        return x+s
            


        
        