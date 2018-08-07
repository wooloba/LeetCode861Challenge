####################
#   Yaozhi Lu      #
#   Aug 7 2018    #
####################
#Origin: https://leetcode.com/problems/power-of-four/description/

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num != 1:
            num /= 4.0
            if num<1:
                return False

        return True


def main():
    so = Solution()
    print(so.isPowerOfFour(12367))


if __name__ == '__main__':
    main()