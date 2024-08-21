'''
https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # m for rows and n for columns
        lenm = len(matrix)
        lenn = len(matrix[0])

        # mn is the list of locations of 0s in matrix
        # i.e. 0 in the middle of 3x3 matrix is [[1,1]]
        mn = []
        for m in range(lenm):
            for n in range(lenn):
                if matrix[m][n] == 0:
                    mn.append([m,n])
                    
        # adjust matrix values to 0s based on the locations of 0s found
        for i in mn:
            # turn 0s to the columns 
            for row in range(lenm):
                matrix[row][i[1]] = 0
            # turn 0s to the rows
            matrix[i[0]] = [0] * lenn
        
