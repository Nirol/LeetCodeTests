class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [ word for word in words if all(letter.lower() in list('qwertyuiop') for letter in word) or all(letter.lower() in list('asdfghjkl') for letter in word) or all(letter.lower() in list('zxcvbnm') for letter in word)]




if(__name__ == "__main__"):
    words = ["Hello", "Alaska", "Dad", "Peace"]
    x = Solution()
    ans = x.findWords(words)
    print(ans)