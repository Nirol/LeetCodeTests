class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s is None:
            return
        length_s=len(s)
        if length_s <= 1:
            return [s]
        ans=[]
        Solution.find_palindromes_rec(self,s, [],ans)
        return ans


    def find_palindromes_rec(self,s,path,ans):
        length_s = len(s)
        if length_s==0:
            ans.append(path)
            return
        if length_s == 1:
            path.append(s)
            ans.append(path)
            return
        for i in range(1,length_s+1):
            first_pal=s[:i]
            if Solution.isPalindrome(self,first_pal) is True:
                Solution.find_palindromes_rec(self,s[i:],path+[first_pal],ans)



    def isPalindrome(self,is_pal):
        rev = is_pal[::-1]
        if (is_pal == rev):
            return True
        return False



if __name__ == "__main__":

    x = Solution()
    print(x.partition("aab"))
