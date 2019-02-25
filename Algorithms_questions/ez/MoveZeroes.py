class Solution(object):
    @staticmethod
    def move_zeroes(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_zeros = nums.count(0)
        nums[:] = (value for value in nums if value != 0)
        for n in range(num_zeros):
            nums.append(0)


if __name__ == "__main__":
    nums = [0,5]
    x = Solution.move_zeroes(nums)
    print(nums)
