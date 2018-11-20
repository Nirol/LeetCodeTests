class Solution:
    def calc(self, inputList):
        min_order=100

        total =list(map(lambda x: x if x[1] >= min_order else (x[0],x[1]+10),map(lambda x: (x[0],x[1]*x[2]),inputList)))
        return total


#
# Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10,- € if the value of the order is less than 100,00 €.
# Write a Python program using lambda and map


if(__name__ == "__main__"):
    inputList = [[34587,4,40.95],[98762,5,56.80],[77226,3,32.95],[88112,3,24.99]]
    x = Solution()
    ans = x.calc(inputList)
    print(ans)