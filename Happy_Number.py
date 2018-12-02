import math
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum=0
        old_sums=[]
        old_sums.append(n)
# my solution is slow
# using  List Comprehensions to get list of digits square:
        #   a=  [(int((str(n))[x])) ** 2 for x in range (0,len(str(n)))]
        # then sum list sum(a)
        # further research can lend better way to find loop of sqaure digits results, either 6 times running or comparing to thes second sum only


        while True:
            n=int(n)
            digits = [int(d) for d in str(n)]
            for d in digits:
                sum=sum + math.pow(d,2)
            if sum == 1:
                return True
            else:
                if sum in old_sums:
                    return False
                old_sums.append(sum)
                n = sum
                sum = 0
        return False





if(__name__ == "__main__"):
    n = 19
    [(int((str(n))[x])) ** 2 for x in range (0,len(str(n)))]
    x = Solution()
    obj = x.isHappy(num)
    print(obj)

