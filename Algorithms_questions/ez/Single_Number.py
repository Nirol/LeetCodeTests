class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for num in nums:
            if num in hash_table:
                del hash_table[num]
            else:
                hash_table[num] = 1
        return hash_table.popitem()[0]
#
# Lesson:
#     1. Using dict with keys to in order to supervised number of copies of each number in nums list
#     2. using popitm() to pop the single item in the dict
#     3. Using math identity = 2∗(a+b+c)−(a+a+b+b+c)=c to find c. will be implemented using python sets:
#        2 * sum(set(nums)) - sum(nums.
#     4.both are 0(n) time and space but ofc using hash its avg O(n) could be worse case.. O(n^2)
#
#     5. Using XOR, ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
#        same thing in python implementation:
#         a = 0
#         for i in nums:
#             a ^= i
#         return a
