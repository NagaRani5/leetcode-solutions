class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for _ in range(n)]
        res=[]
        cols=set()
        dig1=set()
        dig2=set()
        def bt(row):
            if row==n:
                res.append(["".join(row) for row in board])
            for col in range(n):
                if col in cols or (row-col) in dig1 or (row+col) in dig2:
                    continue
                board[row][col]="Q"
                cols.add(col)
                dig1.add(row-col)
                dig2.add(row+col)
                bt(row+1)
                board[row][col]="."
                cols.remove(col)
                dig1.remove(row-col)
                dig2.remove(row+col)
        bt(0)
        return res



        