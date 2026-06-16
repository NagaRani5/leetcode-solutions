class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        s=[]
        r=[]
        a=max(candies)
        for i in candies:
            b=i+extraCandies
            s.append(b)
        for j in s:
            if j<a:
                r.append(bool(0))
            else:
                r.append(bool(1))
        return r


        

        