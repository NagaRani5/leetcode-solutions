class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        for i in range(0,len(nums),2):
            if i+1<len(nums):
                c=c+min(nums[i],nums[i+1])
        return c

        