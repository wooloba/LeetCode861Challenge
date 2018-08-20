####################
#   Yaozhi Lu      #
#   Aug 19 2018    #
####################

#Origin: https://leetcode.com/problems/heaters/description/
import math
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        radius = 0
        for i in range(len(heaters)-1):
            temp = math.ceil(float(abs(houses.index(heaters[i]) - houses.index(heaters[i+1])))//2)
            if temp > radius:
                radius = int(temp)
        
        #left
        if houses.index(heaters[0]) > radius:
            radius = houses.index(heaters[0])
        #right
        right = len(houses) - (houses.index(heaters[-1]) + 1)
        if (right > radius):
            radius = right
        return radius

def main():
    so = Solution()
    A =  [1,2,3]
    B = [2]

    print(so.findRadius(A,B))

if __name__ == '__main__':
    main()