import numpy as np
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pas = []
        for idx in range(numRows):
            tmp_arr= [1] * (idx+1)
            #tmp_arr = np.ones((idx + 1,), dtype=np.int)
            if idx > 1:
                print(idx)
                for j in range(1, idx):
                    print (j)
                    tmp_arr[j] = pas[idx-1][j - 1] + pas[idx-1][j]
            pas.append(tmp_arr)
        return pas



if(__name__ == "__main__"):
    x = Solution()
    ans = x.generate(5)
    print(ans)