class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None:
            return []
        length_digits = len(digits)
        if length_digits == 0:
            return []
        dig_dict = {"2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r","s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y","z"]
                   }

        ans = dig_dict[digits[0]]
        if length_digits == 1:
            return ans
        ans_nxt = []
        for idx, dig in enumerate(digits[1:]):
            for prefix in ans:
                for nxt_dig in dig_dict[dig]:
                    ans_nxt.append(prefix+nxt_dig)
            ans=ans_nxt
            ans_nxt=[]
        return ans

if __name__ == "__main__":
    x = Solution()
    nums1 = "23"
    print(x.letterCombinations(nums1))












