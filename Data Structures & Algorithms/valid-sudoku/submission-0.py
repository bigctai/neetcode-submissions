class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            nums = set()
            for j in range(len(board)):
                if board[i][j] == ".":
                    pass
                else:
                    if board[i][j] in nums:
                        return False
                    else:
                        nums.add(board[i][j])
        for i in range(len(board)):
            nums = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    pass
                else:
                    if board[j][i] in nums:
                        return False
                    else:
                        nums.add(board[j][i])
        for i in range(0, 3, 1):
            for l in range(0, 3, 1):
                nums = set()
                for j in range(0, 3, 1):
                    for k in range(0, 3, 1):
                        x_index = j + 3*i
                        y_index = k + 3*l
                        if board[x_index][y_index] == ".":
                            pass
                        else:
                            if board[x_index][y_index] in nums:
                                return False
                            else:
                                nums.add(board[x_index][y_index])
        return True