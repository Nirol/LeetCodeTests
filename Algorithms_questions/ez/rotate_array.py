class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            temp = nums.pop()
            nums.insert(0, temp)




if __name__ == "__main__":
    x = Solution()
    l = [1,2,3,4,5,6]
    x.rotate(l,3)
    print(l)
