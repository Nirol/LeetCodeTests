class Solution(object):
    def longest_common_sub(self, X,Y):
        """
        :type x,y: string
        :rtype: int
        """
        m=len(X)
        n=len(Y)
        if (m == 0 or n == 0):
            return 0
        memo = [[-1 for y in range(n+1)] for x in range(m+1)]


        for i in range(m+1):
            memo[i][0]=0

        for i in range(n+1):
            memo[0][i]=0

        lcs_length=Solution.dp_lcs(self,X,Y,memo,m,n)

        for i in range(m):
            print(memo[i])

        lcs_backtrk=Solution.backtrack(self,X,Y,memo,m,n)


        print("LCS length = ",lcs_length,", and one backtrack: ",lcs_backtrk)

    def dp_lcs(self,X,Y,memo,m,n):

        if (m == 0 or n == 0):
            return 0
        if (memo[m ][n ] != -1):
            return memo[m ][n ]

        if (X[m-1 ] == Y[n-1]):

            memo[m ][n ] = 1 + Solution.dp_lcs(self,X, Y,memo, m - 1, n - 1)

        else:

            memo[m ][n ] = max(Solution.dp_lcs(self,X, Y,memo, m, n - 1),
                                     Solution.dp_lcs(self,X, Y,memo, m - 1, n))

        return memo[m ][n];

    def backtrack(self,X,Y,memo,m,n):
        if m == 0 or n == 0:
           return ""

        if X[m-1] == Y[n-1]:
            return   Solution.backtrack(self,X,Y,memo,m-1,n-1) +  X[m-1]
        if memo[m][n-1]>memo[m-1][n]:
            return  Solution.backtrack(self,X,Y,memo,m,n-1)
        return  Solution.backtrack(self, X, Y, memo, m-1, n)





if __name__ == "__main__":
    x = Solution()
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    x.longest_common_sub(s1,s2)


