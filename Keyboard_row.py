class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans=0
        for letter in S:
            if letter in J:
                ans=ans+1
        return ans




if(__name__ == "__main__"):
    J = "aA"
    S = "aAAbbbb"
    x = Solution()
    ans = x.numJewelsInStones(J,S)
    print(ans)