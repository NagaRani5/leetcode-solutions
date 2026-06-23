class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def bt(index,path,total):
            if total==target:
                res.append(path[:])
                return
            if total>target or index==len(candidates):
                return
            for i in range(index,len(candidates)):
                path.append(candidates[i])
                bt(i,path,total+candidates[i])
                path.pop()
        bt(0,[],0)
        return res
        