####################
#   Yaozhi Lu      #
#   Sep 2 2018    #
####################

#Origin: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = []
        
        for i in nums:
            if nums[abs(i)-1] < 0:
                pass
            else:
                nums[abs(i)-1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(abs(i)+1)
        
        return output

def main():
    so = Solution()
    A = [4,3,2,7,8,2,3,1]

    print so.findDisappearedNumbers(A)

if __name__ == '__main__':
    main()