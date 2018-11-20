class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        best = -1
        start_indx = 0
        for idx, val in enumerate(bin(N)[2:]):
            print(idx, val)
            if val == '1':
                if (idx - start_indx) > best:
                    print("ong")
                    best=(idx - start_indx)
                start_indx = idx
        return best






if(__name__ == "__main__"):

    x = Solution()
   # ans = x.binaryGap(22)
    for i in range(32):
        print (22>>i)
    print ("lol")
    print(bin(22))
