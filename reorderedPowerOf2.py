import itertools
class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        digList = []
        tmp=N
        while tmp / 10 > 0:
            digList.append(tmp % 10)
            tmp= (tmp//10)
        print (digList)

        numList = list(itertools.combinations(str(digList),len(digList)))

        print (numList)





if(__name__ == "__main__"):
    x = Solution()
    ans = x.reorderedPowerOf2(456)
    print(ans)