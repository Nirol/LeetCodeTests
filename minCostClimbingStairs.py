class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)

    # reccursion is not nesccery here, we can just run one time over the array backwards
    # on each step we can take the min of f1 or f2 when calculating f1!!
    


    #     length_cost=len(cost)
    #     mem = [None] * length_cost
    #     return min(Solution.rec(self,length_cost-1,cost,mem),Solution.rec(self,length_cost-2,cost,mem))
    #
    #
    # def rec(self,idx,cost,mem):
    #
    #     if idx <= 1:
    #         return cost[idx]
    #     jump_one = -1
    #     jump_two = -1
    #     if mem[idx-1] is not None:
    #         jump_one = mem[idx-1]
    #     else:
    #         jump_one = Solution.rec(self,idx-1,cost,mem)
    #         mem[idx-1] = jump_one
    #     if mem[idx-2] is not None:
    #         jump_two = mem[idx-2]
    #     else:
    #         jump_two = Solution.rec(self,idx-2,cost,mem)
    #         mem[idx-2] = jump_two
    #     return min(jump_one+cost[idx],jump_two+cost[idx])










if(__name__ == "__main__"):
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    x = Solution()
    mails = x.minCostClimbingStairs(cost)
    print(mails)