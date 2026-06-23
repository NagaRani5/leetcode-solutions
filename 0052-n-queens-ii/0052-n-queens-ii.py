class Solution:
    def totalNQueens(self, n: int) -> int:
        board=[["."]*n for _ in range(n)]
        self.c=0
        cols=set()
        dig1=set()
        dig2=set()
        def bt(row):
            if row==n:
                self.c+=1
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
        return self.c
        