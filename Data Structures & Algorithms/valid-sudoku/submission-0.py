class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Employ set() as a factory to auto-create an empty set for new keys
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]# [0,(0->8)] ,[1,(0->8)],...
                if val == ".": #ignore "."
                    continue
                if val in rows[r]:#check rows
                    return False 
                if val in cols[c]:#check colomns
                    return False
                square_key = (r // 3, c // 3)# set range of box by divide 3 get 商
                if val in squares[square_key]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[square_key].add(val)
        return True