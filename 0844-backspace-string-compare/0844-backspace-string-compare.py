class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        r=[]
        for i in s:
            if i not in "#":
                r.append(i)
            else:
                if r:
                    r.pop()
        x=[]
        for j in t: 
            if j not in "#":
                x.append(j)
            else:
                if x:
                    x.pop()
        if r==x:
            return True
        else:
            return False       