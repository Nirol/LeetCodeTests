class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        sub_i=sub_v=sub_x=sub_l=sub_c=sub_d = 0
        for c in s[::-1]:
            if c == 'I':
                if sub_i == 0:
                    num = num +1
                else:
                    num = num - 1
            else:
                sub_i=1
                if c == 'V':
                    if sub_v == 0:
                        num = num + 5
                    else:
                        num = num - 5
                else:
                    sub_v=1
                    if c == 'X':
                        if sub_x == 0:
                            num = num + 10
                        else:
                            num = num - 10
                    else:
                        sub_x=1
                        if c == 'L':
                            if sub_l == 0:
                                num = num + 50
                            else:
                                num = num - 50
                        else:
                            sub_l=1
                            if c == 'C':
                                if sub_c == 0:
                                     num = num + 100
                                else:
                                     num = num - 100
                            else:
                                sub_c=1
                                if c == 'D':
                                    if sub_d == 0:
                                        num = num + 500
                                    else:
                                        num = num - 500
                                else:
                                    sub_d = 1
                                    if c is 'M':
                                        num = num + 1000

        return num


if __name__ == "__main__":
    x = Solution()
    num  = x.romanToInt("MCMXCIV")
    print (num)