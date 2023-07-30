"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def withinbounds(a, b):
            "check if an inputted cell in the board"
            if (a>=0 and a<=len(board)-1) and (b>=0 and b<=len(board[0])-1):
                return True
            return False

        def neighbours(i, j):
            # use offset to generate neighbours
            # check if neighbour is within matrix, and not the same element again
            n = []
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if a == 0 and b == 0:
                        continue
                    if withinbounds(i+a, j+b):
                        n.append(board[i+a][j+b])
            return n

        # create auxiliary matrix with same size as board
        aux = [[0 for i in range(len(board[0]))]for j in range(len(board))]

        # fill aux with number of live neighbours
        for i in range(len(aux)):
            for j in range(len(aux[0])):
                n = sum(neighbours(i, j))
                aux[i][j] = n

        #update the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    live = aux[i][j]
                    if live < 2 or live > 3:
                        board[i][j] = 0
                else:
                    live = aux[i][j]
                    if live == 3:
                        board[i][j] = 1


