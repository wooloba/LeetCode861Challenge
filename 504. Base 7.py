####################
#   Yaozhi Lu      #
#   Aug 14 2018    #
####################

#Origin: https://leetcode.com/problems/base-7/description/

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        digits = []
        sign=''
        if num == 0:
            return '0'
        if num<0:
            num*=-1
            sign = '-'
            
        
        while num:
            digits.append(str(num % 7))
            num //= 7 
        digits.append(sign)
        return ''.join(digits[::-1])


def main():
    so = Solution()
    print(so.convertToBase7(0))

if __name__ == '__main__':
    main()