class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ans = []
        for email in emails:
            part1 = email.split('@')
            part2 = part1[0].split('+')
            part3 = part2[0].replace('.', '')
            ans.append(part3+part1[1])
        return ans












if(__name__ == "__main__"):
    mail_address = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    x = Solution()
    mails = x.numUniqueEmails(mail_address)
    print(mails)
