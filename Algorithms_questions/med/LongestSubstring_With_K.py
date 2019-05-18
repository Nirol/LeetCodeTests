# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.
#
#


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))








if __name__ == "__main__":
        x = Solution()
        s1 =[
          [1,1,1],
          [1,0,1],
          [1,1,1]
        ]
        x.longest_common_sub(s1)


