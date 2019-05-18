import numpy as np
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # in order to achive lograitmhic running time
        # we will cut off the array each time our check
        # for the i index does not result in a peak item
        #since nums[i] != nums[i+1] for 0<=i<n we are still promised to fina peak
        # even after cutting the array.


        #for small size inputs I will just use fixed time solution ( better than log)
        # for a faster implementation adn avoiding edge cases.
        len_nums=len(nums)
        if len_nums<10:
            ans=nums[0]
            ans_idx=0
            for indx,i in enumerate(nums):
                if i > ans:
                    ans=i
                    ans_idx=indx
            return ans_idx


        l=0
        r=len_nums-1
        m=int((l+r)/2)
        while 1:
            if nums[m]<nums[m-1]:
                r=m-1
                m=int((l+r)/2)
            elif nums[m]<nums[m+1]:
                l=m+1
                m=int((l+r)/2)
            else:
                return m




if __name__ == "__main__":
    x = Solution()
    nums1 =[1,2,1,3,5,6,4]
    print(x.findPeakElement(nums1))

