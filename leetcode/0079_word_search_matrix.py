
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len = len(board)
        col_len = len(board[0])

        def dfs(i: int, j: int, word_index: int) -> bool:
            if (
                i < 0 or i >= row_len or
                j < 0 or j >= col_len or
                board[i][j] != word[word_index]
            ):
                return False

            print("match found for letter %s at %d %d" % (word[word_index], i, j))

            if word_index + 1 == len(word):
                return True  # word found

            temp, board[i][j] = board[i][j], None
            search_indices = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for search_index in search_indices:
                x = i + search_index[0]
                y = j + search_index[1]
                if dfs(x, y, word_index + 1):
                    return True

            board[i][j] = temp
            return False

        for i in range(row_len):
            for j in range(col_len):
                # print("i, j: %d %d %s", i, j, col)
                if dfs(i, j, 0):
                    return True
        return False


print(Solution().exist([
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]], "ABCCED"))

print(Solution().exist([
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]], "SEE"))


print(Solution().exist([
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]], "ABCB"))
