class Solution:

    def minimumTotal(self, triangle):
        n = len(triangle)
        if n == 0:
            return 0
        if n == 1:
            return triangle[0][0]


        ans_array = []
        for i in range(n):
            ans_array.append([None] * (i+1))
        ans_array[n-1] = triangle[n-1]
        print(triangle[n-1])
        print("lol")
        for row in range(n-2, -1,-1):
            print("****")
            print("row = %d", row)
            for col in range(row+1):
                print("col= %d",col)
                ans_array[row][col]=min(ans_array[row+1][col],ans_array[row+1][col+1])+ triangle[row][col]
                print(ans_array[row][col])
        return ans_array[0][0]























    ## my solution is bad becuase :
    ## i am passing trainagle data everytime, there a way around that
    ## need to use do top down with memoization

    # def minimumTotal(self, triangle):
    #     """
    #     :type triangle: List[List[int]]
    #     :rtype: int
    #     """
    #     if len(triangle) == 0:
    #         return 0
    #     if len(triangle) == 1:
    #         return triangle[0][0]
    #     return Solution.triDP(triangle,0,0,triangle[0][0])
    #
    # def triDP(triangle,row,col,sum):
    #     if row == len(triangle)-1:
    #         return sum
    #     return min(Solution.triDP(triangle,row+1,col,sum+triangle[row+1][col]),Solution.triDP(triangle,row+1,col+1,sum+triangle[row+1][col+1]))







if (__name__ == "__main__"):
    x = Solution()
    triangle=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    ans = x.minimumTotal(triangle)
    print(ans)