class Solution:
    @staticmethod
    def binary_gap(num):
        """
        :type num: int
        :rtype: int
        """
        best = -1
        start_index = 0
        for idx, val in enumerate(bin(num)[2:]):
            print(idx, val)
            if val == '1':
                if (idx - start_index) > best:

                    best = (idx - start_index)
                start_index = idx
        return best


if __name__ == "__main__":
    x = Solution()
    for i in range(32):
        print(22 >> i)
    print(bin(22))
    my_list = [
        1, 2, 3,
        4, 5, 6,
                        ]
