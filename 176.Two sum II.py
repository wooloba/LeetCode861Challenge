####################
#   Yaozhi Lu      #
#   Jul 19 2018    #
####################
#Origin: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        #hash = dict(range(len(numbers)),numbers)
        hash = {}
        for i in range(len(numbers)):
            a = target - numbers[i]
            if hash.get(a) != None:
                return [hash.get(a)+1,i+1]
            else:
                hash[numbers[i]] = i
                
def main():
    solution = Solution()
    print solution.twoSum([0,0,3,4],0)


if __name__ == "__main__":
    main()
