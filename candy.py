class Solution:
    def calc(self, inputList):
        sortedArr = sorted(inputList)
        last_candy=sortedArr[0]
        num_types=1
        for num in sortedArr[1:]:
            if num != last_candy:
                last_candy=num
                num_types = num_types + 1
        if len(sortedArr)/2 < num_types:
            return int(len(sortedArr)/2)
        return num_types

#
# Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10,- € if the value of the order is less than 100,00 €.
# Write a Python program using lambda and map


# Using set:
#
# public class Solution {
#     public int distributeCandies(int[] candies) {
#         HashSet < Integer > set = new HashSet < > ();
#         for (int candy: candies) {
#             set.add(candy);
#         }
#         return Math.min(set.size(), candies.length / 2);
#     }
# }

# or simply return min(len(set(candies)), int(len(candies)/2))


if(__name__ == "__main__"):
    candies = [1, 1, 2, 2, 3, 3]
    x = Solution()
    ans = x.calc(candies)
    print(ans)