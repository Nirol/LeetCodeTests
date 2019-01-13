class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max= float("-inf")
        sec=float("-inf")
        third=float("-inf")
        for n in nums:
            if n > third:
                if n > max:
                    third=sec
                    sec=max
                    max=n
                elif n > sec and n != max:
                    third = sec
                    sec = n
                elif n!=sec and n!=max:
                    third = n
            print("max = %d sec = %d third = %d",max,sec,third)


        if max == sec or sec == third or third == float("-inf"):
            return max
        else:
            return third











if(__name__ == "__main__"):
    x = Solution()
    flowerbed =[1]

    ans = x.thirdMax(flowerbed)
    print (ans)