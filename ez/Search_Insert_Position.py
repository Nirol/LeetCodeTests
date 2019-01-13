
import bisect
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        indx = bisect.bisect_left(nums, target)

        return indx



if(__name__ == "__main__"):
        x = Solution()
        nums = [1,3,5,6]
        target = 0
        ans = x.searchInsert(nums,target)
        print(ans)