class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n = len(matrix[0])
        if m == 0:
            return

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for i_curr in range(m):
                        if matrix[i_curr][j] != 0:
                            matrix[i_curr][j]='a'

                    for j_curr in range(n):
                        if matrix[i][j_curr] != 0:
                            matrix[i][j_curr] = 'a'

        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='a':
                    matrix[i][j] =0











if __name__ == "__main__":
        x = Solution()
        s1 =[
          [1,1,1],
          [1,0,1],
          [1,1,1]
        ]
        x.longest_common_sub(s1)


