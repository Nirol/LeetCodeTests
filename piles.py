import math
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = list()
        if n == 1:
            ans.append(str(1))
            return ans
        if n == 2:
            ans.append(str(1))
            ans.append(str(2))
            return ans
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                 ans.append("FizzBuzz")

            elif i % 3 == 0 :
                ans.append("Fizz")

            elif i % 5 == 0 :
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans





if(__name__ == "__main__"):

    x = Solution()
    #ans = x.stoneGame(candies)
    print(x.fizzBuzz(16))