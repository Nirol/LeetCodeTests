import math
class Solution:
    def reverse(self, x: int) -> int:

        ans=0
        flag_minus=0
        if x < 0 :
            flag_minus = 1
        x= int(math.fabs(x))
        num_digits = len(str(x))
        while x:
            digit = x % 10
            ans = int(ans + digit*(math.pow(10,num_digits-1)))
            num_digits=num_digits-1
            x = x // 10
        if flag_minus==1:
            ans=ans*-1
       # if ans > sys.maxsize or ans < -sys.maxsize - 1:
        if ans >  math.pow(2,31) -1 or ans < -1*(math.pow(2,31)):
            return 0
        return ans



if __name__ == "__main__":
    x = Solution()
    ans = x.reverse(-123)
    print(ans)
