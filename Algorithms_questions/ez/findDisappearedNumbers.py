class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## not my sol:
        # substracting the real set from the full set gives the missing numbers.
        return list(set(range(1, len(nums) + 1)) - set(nums))







if __name__ == "__main__":
    x = Solution()
    llist =[4,3,2,7,8,2,3,1]
    list2=[1,1]
    ans = x.findDisappearedNumbers(llist)
    print(ans)

