from typing import List


class Solution:
    def permute(self, nums):
        return nums and [p[:i] + [nums[0]] + p[i:]
                         for p in self.permute(nums[1:])
                         for i in range(len(nums))] or [[]]



if __name__ == "__main__":
    x = Solution()
    nums1  = [1, 2, 3]
    nums1.
    print(x.permute(nums1))

