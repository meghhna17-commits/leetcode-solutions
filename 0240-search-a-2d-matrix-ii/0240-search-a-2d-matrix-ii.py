class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix[0])
        n=len(matrix)
        col=m-1
        row=0
        while(row<n and col>=0):
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col=col-1
            else:
                row=row+1
        return False 
        