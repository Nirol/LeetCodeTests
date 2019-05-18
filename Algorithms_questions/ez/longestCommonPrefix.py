class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        min_length = min([len(x) for x in strs])
        ans=""
        for i in range(min_length):
            chars_set = set([c[i] for c in strs])
            if len(chars_set) > 1 :
                return ans
            else:
                ans = ans + strs[0][i]

        return ans


if __name__ == "__main__":
    x = Solution()
    llist =["dog","racecar","car"]
    ans = x.longestCommonPrefix(llist)
    print(ans)

