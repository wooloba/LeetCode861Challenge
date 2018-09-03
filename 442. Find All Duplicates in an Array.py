####################
#   Yaozhi Lu      #
#   Sep 2 2018    #
####################

#Origin: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = []
        for i in nums:
            
            if nums[abs(i)-1] < 0:
                output.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        
        return output

def main():
    so = Solution()
    A = [4,3,2,7,8,2,3,1]
    print so.findDuplicates(A)

if __name__ == '__main__':
    main()

    

