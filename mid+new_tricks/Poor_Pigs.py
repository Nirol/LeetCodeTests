import math
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):

        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """

        pigs = math.log(buckets, 1+ math.floor(minutesToTest // minutesToDie))
        print (pigs)
        return int(math.ceil(pigs))

       # sol is   (⌊minutesToTest / minutesToDie⌋ + 1)pigs
        # basiclly each pig drink a whole row of a dim in each test
        # we have (minutesToTest / minutesToDie) tests meaning the size of the square ( both row and col ) is tests+1.
        #last row of each dim is given for free since its enough to check the first n-1 rows and if the pig dont die its the last one.
        # on each test each pig drink a whole row if he dies after 15 min we only know the row from that pig
        # combination of the rows of all pigs give the exact coordinate.
        # in the given example: we can do 4 tests ==> size of square is 5.
        # 5 pigs give us 5 dims, == number of total buckets we are able to check is 3125
        #if we would of tried using 4 pigs we could of check only dim 4, 4^4=256. not enough for 1k buckets.









if(__name__ == "__main__"):
    buckets=1000
    minutesToDie=15
    minutesToTest=60
    x = Solution()
    obj = x.poorPigs(buckets,minutesToDie,minutesToTest)
    print(obj)

