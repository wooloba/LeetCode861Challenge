####################
#   Yaozhi Lu      #
#   Nov 18 2018    #
####################

#Origin: https://leetcode.com/problems/max-consecutive-ones/

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return len(max(''.join(str(x) for x in nums).split(str(0))))

def main():
    nums = [1,1,0,1,1,1]
    so = Solution().findMaxConsecutiveOnes(nums)
    print(so)

if __name__ == "__main__":
    main()
