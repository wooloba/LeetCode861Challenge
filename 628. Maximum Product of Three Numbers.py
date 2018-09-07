####################
#   Yaozhi Lu      #
#   Sep 6 2018    #
####################

#Origin:https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse = True)
        return max(nums[0]*nums[1]*nums[2],nums[0]*nums[-1]*nums[-2])


def main():
    so = Solution()
    A = [-4,-3,-2,-1,60]
    #[1,2,3,4]

    print so.maximumProduct(A)


if __name__ == '__main__':
    main()