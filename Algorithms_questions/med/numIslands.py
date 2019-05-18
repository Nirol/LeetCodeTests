class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        grid_ver = len(grid)
        if grid_ver == 0:
            return 0
        grid_horz = len(grid[0])
        if grid_horz == 0:
            return 0
        rows, cols = (grid_ver, grid_horz)

        memo_grid = [[0 for i in range(cols)] for j in range(rows)]

        for i in range(grid_ver):
            for j in range(grid_horz):
                if grid[i][j] == "1" and memo_grid[i][j] == 0:
                    islands = islands + 1
                    memo_grid[i][j] = 1
                    Solution.numIslands_rec(self, grid, i + 1, j, grid_ver,
                                            grid_horz, memo_grid)
                    Solution.numIslands_rec(self, grid, i, j + 1, grid_ver,
                                            grid_horz, memo_grid)
        return islands

    def numIslands_rec(self, grid, i, j, grid_ver, grid_horz, memo_grid):
        if i > grid_ver - 1 or j > grid_horz - 1:
            return
        if grid[i][j] == "0":
            return
        if memo_grid[i][j] == 1:
            return
        memo_grid[i][j] = 1
        if j - 1 >= 0:
            # go left
            Solution.numIslands_rec(self, grid, i, j - 1, grid_ver, grid_horz,
                                    memo_grid)
        if j + 1 <= grid_horz - 1:
            # go right
            Solution.numIslands_rec(self, grid, i, j + 1, grid_ver, grid_horz,
                                    memo_grid)
        if i + 1 <= grid_ver - 1:
            # go down
            Solution.numIslands_rec(self, grid, i + 1, j, grid_ver, grid_horz,
                                    memo_grid)
        if i -1 >= 0:
           #go up
            Solution.numIslands_rec(self, grid, i -1, j, grid_ver, grid_horz,
                                    memo_grid)

if __name__ == "__main__":
    x = Solution()
    nums1 =[["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
    print(x.numIslands(nums1))






