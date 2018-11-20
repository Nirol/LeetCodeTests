import copy
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        Solution.recc(self,0,candidates,target,None,ans)
        return ans
    def recc(self,idx,candidates,target,seq,ans):
        print("target =",target,", seq= ",seq," idx = ",idx)
        if target == 0:
            ans.append(seq)
            return
        if target < 0 :
            return
        indx=idx
        while indx <= len(candidates)-1:
            if candidates[indx] <= target:
                if seq is None:
                    new_seq = []
                else:
                    new_seq = copy.deepcopy(seq)
                new_seq.append(candidates[indx])
                Solution.recc(self,indx,candidates,target-candidates[indx],new_seq,ans)
            indx+=1




if(__name__ == "__main__"):
    candidates = [2,3,5]
    target = 8
    x = Solution()
    ans = x.combinationSum(candidates,target)
    print(ans)