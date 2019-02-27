import math
class Solution:
    def countPrimes(self, n: int) -> int:
        ans=0
        for i in range (n):
            if Solution.is_prime(i):
                ans=ans+1

        return ans



    def is_prime(n):
            if n == 2:
                return True
            if n % 2 == 0 or n <= 1:
                return False

            sqr = int(math.sqrt(n)) + 1

            for divisor in range(3, sqr, 2):
                if n % divisor == 0:
                    return False
            return True







if __name__ == "__main__":
    x = Solution()
    ans = x.countPrimes(10)
    print(ans)
