class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]
        
        # Track occupied paths
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)
        
        def backtrack(r: int):
            # Base Case: All queens are successfully placed
            if r == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            
            # Try placing a queen in each column of row r
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # Place the queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                # Move to the next row
                backtrack(r + 1)
                
                # Backtrack and remove the queen
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
                
        backtrack(0)
        return ans
