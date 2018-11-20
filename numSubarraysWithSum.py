class Solution:
    def numSubarraysWithSum(self, A ,S ):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """

        #the whole trick here is to create an array with indx of 1 occurnces only
        # after thats its easy to understand between adjecent cells in the array
        # how many 0's are between them and to multiply the number of 0's at start with
        # the numbers of 0's at the end
        indexes = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)]
        print (indexes)








if(__name__ == "__main__"):
    A = [1,0,1,0,1,0,0,1]
    S = 2
    x = Solution()
    mails = x.numSubarraysWithSum(A,S)
    print(mails)