class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # FIBBONACI SOL
        if n == 1 :
            return 1


        first = 1
        second =2

        for i in range (3,n):
            third = first+second
            first= second
            second=third

        return second



        #DP SOLUTION:
        #
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # ways = [None] * n
        # ways[n - 1] = 1
        # ways[n - 2] = 2
        #
        # for i in range(n - 3, -1, -1):
        #     ways[i] = ways[i + 1] + ways[i + 2]
        # return ways[0]
