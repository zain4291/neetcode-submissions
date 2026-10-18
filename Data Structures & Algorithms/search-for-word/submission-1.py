class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            directions = [[1,0], [-1,0], [0, 1], [0, -1]]
            
            if (r < 0 or c < 0 or r >= rows or c >= cols) or board[r][c] != word[i] or (r, c) in path:
                return False
            
            path.add((r, c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    return True
            path.remove((r, c))
            return False




        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
                
