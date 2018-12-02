class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for leetter in letters:
            if leetter > target:
                return(leetter)


if(__name__ == "__main__"):
    letters = ["c", "f", "j"]
    target = "c"
    x = Solution()
    letter = x.nextGreatestLetter(letters,target)
    print(letter)