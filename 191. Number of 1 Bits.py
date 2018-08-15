####################
#   Yaozhi Lu      #
#   Aug 14 2018    #
####################

#Origin :https://leetcode.com/problems/number-of-1-bits/description/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        A = bin(n)[2:]

        num = 0
        for i in A:
            num += int(i)
        
        return num

def main():
    so = Solution()
    print(so.hammingWeight(11))

if __name__ == '__main__':
    main()