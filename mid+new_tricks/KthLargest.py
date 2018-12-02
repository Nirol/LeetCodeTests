import heapq
class KthLargest:

    def __init__(self, k, nums):





        #my sol is right but bad cause I implemented priority queue by myself instead of using known tools
        # using heapq.heapify of python:
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

    #     """
    #     :type k: int
    #     :type nums: List[int]
    #     """
    #     nums.sort()
    #     self.k = k
    #     self.sorted_array_top=[]
    #     if len(nums) <=k:
    #         self.sorted_array_top = nums
    #     else:
    #         self.sorted_array_top = nums[len(nums)-self.k:]
    #
    #
    #
    #
    #
    # def add(self, val):
    #     """
    #     :type val: int
    #     :rtype: int
    #     """
    #     print(self.sorted_array_top)
    #     if len(self.sorted_array_top) < self.k:
    #         KthLargest.insert_in_place(self,val)
    #     elif val > self.sorted_array_top[0]:
    #         KthLargest.insert_in_place(self,val)
    #         if len( self.sorted_array_top) > self.k:
    #             self.sorted_array_top=self.sorted_array_top[1:]
    #     return self.sorted_array_top[0]
    #
    # def insert_in_place(self,val):
    #     if len(self.sorted_array_top) == 0:
    #         self.sorted_array_top=[val]
    #     else:
    #         for idx, value in enumerate(self.sorted_array_top):
    #             if val <= value:
    #                 self.sorted_array_top[idx:idx] = [val]
    #                 break
    #         if val > self.sorted_array_top[len(self.sorted_array_top)-1]:
    #             self.sorted_array_top.append(val)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if(__name__ == "__main__"):
    nums = [1,-2];
    obj = KthLargest(3, nums)

    print(obj.add(-3)); # returns    4
    print(obj.add(0)); # returns    5
    print(obj.add(2)); # returns    5
    print(obj.add(-1)); # returns    8
    print(obj.add(4)); # returns    8







