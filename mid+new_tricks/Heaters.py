import math
import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

    # binary search in python, with the usage of float inf as edges for correctnoes .
        heaters.sort()

        ans = 0

        for h in houses:
            hi = bisect.bisect_left(heaters, h)
            left = heaters[hi - 1] if hi - 1 >= 0 else float('-inf')
            right = heaters[hi] if hi < len(heaters) else float('inf')
            ans = max(ans, min(h - left, right - h))
        return ans


if(__name__ == "__main__"):
    heaters =  [1,4]
    houses =  [1,2,3,4]
    x = Solution()
    letter = x.findRadius(houses,heaters)
    print(letter)