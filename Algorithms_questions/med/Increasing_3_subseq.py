class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False









if __name__ == "__main__":
    x = Solution()
    nums1 =[1,2,1,3,5,6,4]
    print(x.increasingTriplet(nums1))

