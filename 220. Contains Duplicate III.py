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
        
        #time limit exceed
        dic = dict(zip([i for i in range(0,len(nums))],nums))
        for i in range(len(dic)-1):
            for j in range(i+1,len(dic)):
                print(i,j)
                if abs(i-j) > k:
                    break
                if abs(dic[i] - dic[j])<= t:
                    return True
        return False

def main():
    so = Solution()
    print(so.containsNearbyAlmostDuplicate([1,2,3,1],3,0))

if __name__ == "__main__":
    main()




