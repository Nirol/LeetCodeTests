class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_length = len(needle)
        haystack_length = len(haystack)
        if needle_length is 0:
            return 0
        for i in range(0,(haystack_length - needle_length)+1):
            substr = haystack[i:i+needle_length]
            if substr == needle:
                return i
        return -1




if __name__ == "__main__":
    x = Solution()
    haystack = "hello"
    needle = "lo"
    print(x.strStr(haystack,needle))
