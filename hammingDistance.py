class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor_opt=x^y
        strr=str(bin(xor_opt))
        return strr.count('1')




if(__name__ == "__main__"):
    x = Solution()
    mails = x.hammingDistance(1,4)
    print(mails)