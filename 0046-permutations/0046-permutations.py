class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def bt(path):
            if len(nums)==len(path):
                res.append(path[:])
                return
            for i in nums:
                if i not in path:
                    path.append(i)
                    bt(path)
                    path.pop()
        bt([])
        return res

        