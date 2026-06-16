class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        r=[]
        for i in nums:
            s+=i
            r.append(s)
        return r

        