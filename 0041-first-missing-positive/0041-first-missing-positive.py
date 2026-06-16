class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        k=1
        while True:
            if k not in s:
                return k
                break
            k+=1
        else:
            return k
        