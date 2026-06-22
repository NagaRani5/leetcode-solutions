class Solution:
    def findLucky(self, arr: List[int]) -> int:
        r=[]
        for i in arr:
            if i==arr.count(i):
                r.append(i)
        if r:
            return max(r)
        else:
            return -1

                