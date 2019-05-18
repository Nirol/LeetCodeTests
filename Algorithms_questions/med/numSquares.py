import math
import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0

        #list of solutions, the i slot is the solution for i.
        num_sqr_list=[0]
        #building the solutions list from 1 till n:
        for i in range(1,n+1):
            curr_size=len(num_sqr_list)
            # next_pr_sqr represents the next perfect sqr solution,
            # initialized to n+1 , promised to be bigger than the answer
            next_pr_sqr=n+1

            #calculation itself is done by iterating numbers between 1 to the closet
            # square root, reducing the square of the number from the current target: curr_size-j*j
            # num_sqr_list[curr_size-j*j] will hold the result for curr_size-j*j , adding 1 for j*j itself.
            for j in range(1,int(math.sqrt(curr_size))+1):
                next_pr_sqr=min(next_pr_sqr,num_sqr_list[curr_size-j*j]+1)
            num_sqr_list.append(next_pr_sqr)

        return num_sqr_list[n]


if __name__ == "__main__":
    x = Solution()
    nums1 =12
    print(x.numSquares(nums1))

