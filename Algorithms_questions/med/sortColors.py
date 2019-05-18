class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        #counting sort is the go-to solution, fitting to the problem of sorting n objects in limitied range.
        #different solution with only a single passage on the array I came up with:
        # partitoning the array to sorted 0'(left index) sortes 2's  (right index )and unclassified (center index)
        # if you encounter 2 on the right side you move on.
        # encountering 2 on the left or 0 on the right you insert it to the opposite index and move on.

        if len(nums)<2:
            return
        length_nums=len(nums)
        if length_nums <2:
            return
        l_index=0
        r_index=len(nums)-1
        c_index=0
        while c_index<=r_index:
            if nums[c_index] is 0:
                nums[l_index], nums[c_index] = nums[c_index],nums[l_index]
                l_index=l_index+1
                c_index=c_index+1
            elif nums[c_index] is 1:
                c_index=c_index+1
            else:
                nums[r_index], nums[c_index] = nums[c_index],nums[r_index]
                r_index=r_index-1



if __name__ == "__main__":
    x = Solution()
    nums1 = [0,0,0,1]
    nums2=[2,0,2,1,1,0]
    nums3=[2,0,2,1,1,0,2,2,2,0,0,0,2]
    x.sortColors(nums1)
    print(nums1)








