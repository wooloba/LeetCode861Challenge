####################
#   Yaozhi Lu      #
#   Nov 14 2018    #
####################

#Origin: https://leetcode.com/problems/contains-duplicate-iii/

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        
        dic = dict(zip([i for i in range(0,len(nums))],nums))
        dic = sorted(dic.items(),key= lambda x:x[1])


        for i in range(len(dic)-1):
            if abs(dic[i][1] - dic[i+1][1]) > t:
                break
            for j in range(i+1,len(dic)):
                print(i,j)
                if abs(dic[i][0] - dic[j][0])<= k and abs(dic[i][1] - dic[j][1])<=t and dic[i][1] != dic[j][1]:
                    return True
                
        return False

def main():
    so = Solution()
    print(so.containsNearbyAlmostDuplicate([-1,-1],1,0))

if __name__ == "__main__":
    main()




