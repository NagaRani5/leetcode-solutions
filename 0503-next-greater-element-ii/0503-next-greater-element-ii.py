class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        a=nums+nums
        y=len(a)
        r=[]
        for i in range(len(nums)):
            x=nums[i]
            b=a[i+1:y]
            for j in b:
                if j>x:
                    r.append(j)
                    break
            else:
                r.append(-1)
        return r


        
        