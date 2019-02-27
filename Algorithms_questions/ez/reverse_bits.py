class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            # shifting res one bit to the left and adding the right most bit by and wise with the binary number 00000001 ( will take only the left most bit value from n
            res = (res << 1) + (n & 1)
            # shifting n to the left 1 bit
            n >>= 1
        return res






if __name__ == "__main__":
    x = Solution()
    numb=782
    print(bin(numb))
    ans = x.reverseBits(numb)
    print(ans)

