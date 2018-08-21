####################
#   Yaozhi Lu      #
#   Aug 21 2018    #
####################

#Origin: https://leetcode.com/problems/majority-element/description/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if dic.get(i) == None:
                dic[i] = 1
            else:
                dic[i] += 1
                
            if dic[i] > len(nums)//2.0:
                return i


def main():
    A = [2,2,1,1,1,2,2]
    so = Solution()
    print(so.majorityElement(A))

if __name__ == '__main__':
    main()