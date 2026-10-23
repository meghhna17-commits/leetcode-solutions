class Solution(object):
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])

        low = 0
        high = m - 1

        while low <= high:
            mid = (low + high) // 2

            maxRow = 0

            for i in range(n):
                if mat[i][mid] > mat[maxRow][mid]:
                    maxRow = i

            if mid - 1 >= 0:
                left = mat[maxRow][mid - 1]
            else:
                left = -1

            if mid + 1 < m:
                right = mat[maxRow][mid + 1]
            else:
                right = -1

            if mat[maxRow][mid] > left and mat[maxRow][mid] > right:
                return [maxRow, mid]

            elif mat[maxRow][mid] < right:
                low = mid + 1

            else:
                high = mid - 1

        