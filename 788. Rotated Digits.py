####################
#   Yaozhi Lu      #
#   Sep 2 2018    #
####################

#Origin:https://leetcode.com/problems/rotated-digits/description/

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = 0
        
        for i in range(0,N+1):
            if '3' in str(i) or '4' in str(i) or '7' in str(i):
                continue
            elif '2' in str(i) or '5' in str(i) or '6' in str(i) or '9' in str(i) :
                num += 1

        return num
    
def main():
    so = Solution()

    print so.rotatedDigits(2)


if __name__ == '__main__':
    main()

