####################
#   Yaozhi Lu      #
#   Aug 24 2018    #
####################

#Origin: https://leetcode.com/problems/power-of-two/description/

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n != 1:
            n /= 2.0
            if n%1 != 0:
                return False
        
        return True


def main():
    so = Solution()

    print so.isPowerOfTwo(0)

if __name__ == '__main__':
    main()