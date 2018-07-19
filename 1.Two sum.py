####################
#   Yaozhi Lu      #
#   Jul 18 2018    #
####################
#Origin: https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]+nums[i] == target:
                    return[i,j]
                else:
                    pass


def main():
    solution = Solution()
    print solution.twoSum([3,2,4],6)


if __name__ == "__main__":
    main()