class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        #starting from last row so moving back only by row and fixing up by moving to upper col
        #could potentally move right to next col and yet again move up to an upper row.
        if matrix:
            row, col, width = len(matrix) - 1, 0, len(matrix[0])
            while row >= 0 and col < width:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    row = row - 1
                else:
                    col = col + 1
            return False





if __name__ == "__main__":
    x = Solution()
    nums1 = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 13, 19],
      [3,   6,  9, 16, 22],
      [10, 11, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    print(x.searchMatrix(nums1,13))
