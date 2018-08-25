####################
#   Yaozhi Lu      #
#   Aug 24 2018    #
####################

#Origin: https://leetcode.com/problems/power-of-three/description/

import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return 1162261467%n == 0


    

def main():
    so = Solution()

    print so.isPowerOfThree(27)

if __name__ == '__main__':
    main()