class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        temp1 = S.split("-")
        string1=""
        string2=string1.join(temp1)
        string2=string2.upper()[::-1]
        res = '-'.join([string2[i:i + K] for i in range(0, len(string2), K)])
        print(temp1)
        print(string2)
        print(res)
        return res[::-1]







if(__name__ == "__main__"):
    x = Solution()
    S ="2-5g-3-J"
    K= 2
    ans = x.licenseKeyFormatting(S,K)
    print(ans)