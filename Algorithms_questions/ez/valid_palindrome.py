class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(ch for ch in s if ch.isalnum())
        s_length = len(s)
        if s is None or s_length == 0 or s_length == 1:
            return True
        print(s_length)

        for i in range(s_length):
            print("********")
            print("i=",i)
            print("s_length-1-i",s_length-1-i)
            print(s[i])
            print(s[s_length-1-i])
            print("********")
            if i < s_length-1-i:
                if s[i].lower() != s[s_length-1-i].lower():
                    return False
            else:
                return True







if __name__ == "__main__":
    x = Solution()
    l = "A man, a plan,%^&^%&#!# a canal: Panama"
    print(x.isPalindrome(l))
