import copy
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if m == 0:
            nums1[0:] = nums2[0:]
            return
        if n == 0:
            return
        temp1 = nums1[:m]
        index_1 = 0
        index_2 = 0
        for i in range(m + n):
            if temp1[index_1] <= nums2[index_2]:
                nums1[i] = temp1[index_1]
                index_1 = index_1 + 1
                if index_1 == m :
                    nums1[i+1:] = nums2[index_2:]
                    return
            else:
                nums1[i] = nums2[index_2]
                index_2 = index_2 + 1
                if index_2 == n :
                    nums1[i+1:] = temp1[index_1:]
                    return


if __name__ == "__main__":
    x = Solution()
    nums1 = []
    m=0
    nums2=[1]
    n=1
    x.merge(nums1,m,nums2,n)
    print(nums1)

