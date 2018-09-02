####################
#   Yaozhi Lu      #
#   Sep 1 2018    #
####################

#Origin:https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        maxLen = 1

        seq = [nums[0]]
        for i in range(1,len(nums)):
            
            if nums[i] > nums[i-1]:
                seq.append(nums[i])
            else:
                seq = [nums[i]]
            if len(seq) > maxLen:
                maxLen = len(seq)
        
        return maxLen

def main():
    so = Solution()
    A = [1,3,5,7]

    print so.findLengthOfLCIS(A)

if __name__ == '__main__':
    main()