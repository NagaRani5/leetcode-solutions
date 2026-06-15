class Solution:
    def calPoints(self, operations: List[str]) -> int:
        r=[]
        for i in operations:
            if i not in "CD+": 
                r.append(int(i))
            elif i in "C":
                r.pop()
            elif i in "D":
                r.append(r[-1]*2)
            elif i in "+":
                    b=r[-1]+r[-2]
                    r.append(b)
        return sum(r)

        