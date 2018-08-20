####################
#   Yaozhi Lu      #
#   Aug 19 2018    #
####################

#Origin: https://leetcode.com/problems/heaters/description/
import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()

        dis = []
        for j in houses:
            pos = bisect.bisect(heaters, j)
            if pos >=1 :
                if  pos >= len(heaters):
                    pos -= 1
                dis.append(min(abs(heaters[pos] - j), abs(heaters[pos-1] - j)))
            else:
                dis.append(abs(j-heaters[0]))
        
        return max(dis)

        

        # for i in range(len(heaters)-1):
        #     temp = math.ceil(float(abs(houses.index(heaters[i]) - houses.index(heaters[i+1])))//2)
        #     if temp > radius:
        #         radius = int(temp)
        
        # #left
        # if houses.index(heaters[0]) > radius:
        #     radius = houses.index(heaters[0])
        # #right
        # right = len(houses) - (houses.index(heaters[-1]) + 1)
        # if (right > radius):
        #     radius = right
        

def main():
    so = Solution()
    A =  [1,1,1,1,1,1,999,999,999,999,999]

    B = [499,500,501]

    print(so.findRadius(A,B))

if __name__ == '__main__':
    main()