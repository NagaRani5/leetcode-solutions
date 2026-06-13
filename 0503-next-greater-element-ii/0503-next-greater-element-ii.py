class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        a=[-1]*len(nums)
        for i in range(2*len(nums)-1,-1,-1):
            index=i%len(nums)
            while stack and stack[-1]<=nums[index]:
                stack.pop()
            if stack:
                a[index]=stack[-1]
            stack.append(nums[index])
        return a 


        
        