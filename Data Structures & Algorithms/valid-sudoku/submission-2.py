class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = defaultdict(set)
        
        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                if board[r][c] in seen[(r , c)]:
                    return False
                
                if board[r][c] in seen[(c , r)]:
                    return False
                
                if board[r][c] in seen[(r // 3, c // 3)]: 
                    return False
                
                seen[r].add(board[r][c])
                seen[c].add(board[r][c])
                seen[(r // 3, c // 3)].add(board[r][c])

        
        return True