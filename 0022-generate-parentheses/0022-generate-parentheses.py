class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r=[]
        def bt(path):
            open=path.count("(")
            close=path.count(")")
            if len(path)==2*n:
                r.append("".join(path))
                return
            if open<n:
                path.append("(")
                bt(path)
                path.pop()
            if close<open:
                path.append(")")
                bt(path)
                path.pop()
        bt([])
        return r
    
            