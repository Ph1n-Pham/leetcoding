"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 
Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        create lists of combination of rows/cols/sub-boxes 
        that need to be checked
        then check if all of them satisfied
        '''
        listRow = []
        listCol = ["","","","","","","","",""]
        listBox = ["","","","","","","","",""]
        for r in range(0,9):
            #row combination
            temp_str = ''.join(str(i) for i in board[r] if i != ".")
            listRow.append(temp_str)

            for i in range(0,9):
                if board[r][i]!= ".":
                    #col combinations
                    listCol[i] += board[r][i]
                    #sub-box combinations
                    listBox[r//3*3 + i//3] += board[r][i]

        def checkDuplicate(s):
            "True if there is duplicate in s"
            alphabet = "123456789"
            for i in s:
                count = s.count(str(i))
                if count > 1:
                    return True
            return False

        #check validation
        for lst in [listRow, listCol, listBox]:
            for checkStr in lst:
                if checkDuplicate(str(checkStr)):
                    return False
        return True
