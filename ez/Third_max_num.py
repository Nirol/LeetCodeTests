class Solution(object):
    @staticmethod
    def third_max(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_max = float("-inf")
        sec = float("-inf")
        third = float("-inf")
        for n in nums:
            if n > third:
                if n > first_max:
                    third = sec
                    sec = first_max
                    first_max = n
                elif n > sec and n != first_max:
                    third = sec
                    sec = n
                elif n != sec and n != first_max:
                    third = n
            print("first_max = %d sec = %d third = %d", first_max, sec, third)

        if first_max == sec or sec == third or third == float("-inf"):
            return first_max
        else:
            return third


if __name__ == "__main__":
    flowerbed = [1]
    ans = Solution.third_max(flowerbed)
    print(ans)
