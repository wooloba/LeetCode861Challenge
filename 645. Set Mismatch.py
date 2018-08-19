####################
#   Yaozhi Lu      #
#   Aug 19 2018    #
####################

#Origin: https://leetcode.com/problems/set-mismatch/description/

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n = len(nums)

        # re = [-1,-1]
        # for i in range(n):
        #     c = nums.count(i+1)
        #     if c == 0:
        #         re[1] = i+1
        #     elif c == 2:
        #         re[0] = i+1

        re = [-1,-1]
        k = [-1] * len(nums)

        for i in nums:
            if k[i-1] != -1:
                re[0] = i
            else:
                k[i-1] = i
        
        re[1] = k.index(-1)+1
        

        return re

def main():
    A = [1,1]
    so = Solution()

    print so.findErrorNums(A)

if __name__ == '__main__':
    main()