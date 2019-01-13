class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """




        ##
        # better solution: add 0 at first and end spot to cancel the requirement of edge cases. 
        #
        #





        planted=0
        temp_streak_counter=0
        if flowerbed[0]==0:
            first_streak=1
        else:
            first_streak=0

        for i,f in enumerate(flowerbed):
            if f is 0:
                temp_streak_counter=temp_streak_counter+1
                if i is len(flowerbed)-1:
                    print("Location = ", i, ", Streak = ", temp_streak_counter)
                    print("planted=",planted)
                    if temp_streak_counter == len(flowerbed) and ( temp_streak_counter % 2 ==1):
                        planted = planted + (temp_streak_counter // 2) +1
                    else:
                        planted  = planted +  (temp_streak_counter// 2)
                    print("planted=", planted)
            else:
                print ("Location = ",i,", Streak = ",temp_streak_counter)
                if temp_streak_counter % 2 is 0:
                    if first_streak is 1:
                        planted = planted+ temp_streak_counter // 2
                    else:
                        planted =planted + max(0,temp_streak_counter//2 -1)
                else:
                    print ("Adding: ",temp_streak_counter // 2)
                    planted =planted+ temp_streak_counter // 2
                first_streak=0
                temp_streak_counter=0
            if planted >= n:
                return True
        print (planted)
        return False










if(__name__ == "__main__"):
    x = Solution()
    flowerbed =[0]
    n=1
    print (2//2)
    ans = x.canPlaceFlowers(flowerbed,n)
    print (ans)