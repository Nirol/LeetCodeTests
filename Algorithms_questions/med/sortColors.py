class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        one_idx = zero_count
        one_count = nums.count(1)
        two_idx = one_count + zero_count

        length_nums = len(nums) - 1

        l =0
        r = length_nums
        while  l < zero_count and r >= two_idx:
            while nums[one_idx] == 1 and one_idx < length_nums:
                one_idx +=1
            while nums[l] == 0 and l < length_nums:
                l+=1
            while nums[r] == 2 and r >=0:
                r-=1

            if nums[l] == 2 and nums[r] == 0:
                Solution.swap(nums,l,r)
            if nums[l] == 1 and l < zero_count:
                Solution.swap(nums, l, one_idx)
                one_idx+=1
            if nums[r] == 1 and r >= two_idx:
                Solution.swap(nums, r, one_idx)
                one_idx+=1


    def swap(A,l,r):
        temp = A[l]
        A[l] = A[r]
        A[r] = temp



if __name__ == "__main__":
    x = Solution()
    nums1 = [0,0,0,1]
    nums2=[2,0,2,1,1,0]
    nums3=[2,0,2,1,1,0,2,2,2,0,0,0,2]
    x.sortColors(nums1)
    print(nums1)
    x.sortColors(nums2)
    print(nums2)
    x.sortColors(nums3)
    print(nums3)









