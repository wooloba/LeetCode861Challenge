####################
#   Yaozhi Lu      #
#   Aug 12 2018    #
####################

#Origin:https://leetcode.com/problems/find-pivot-index/description/

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        asum = sum(nums)
        bsum = 0
        for i in range(len(nums)):
            if i != 0:
                bsum += nums[i-1]
            asum -= nums[i]

            if bsum == asum:
                return i
        return -1
        
def main():
    A = [1, 2, 3]
    so = Solution()
    print(so.pivotIndex(A))

if __name__ == '__main__':
    main()