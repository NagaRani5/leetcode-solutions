class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        r=[]
        for i in range(1,n+1):
            if i in target and i<=target[-1]:
                r.append("Push")
            elif i not in target and i<=target[-1]:
                r.append("Push")
                r.append("Pop")
        return r




        