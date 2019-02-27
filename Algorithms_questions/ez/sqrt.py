class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        if x<=2:
            return 1
        for i in range(2,x):
            if i * i > x:
                return i - 1
            if i*i == x:
                return i



if __name__ == "__main__":
    x = Solution()
    print(x.mySqrt(25))

