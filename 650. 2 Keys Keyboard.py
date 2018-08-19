####################
#   Yaozhi Lu      #
#   Aug 19 2018    #
####################

# Origin: https://leetcode.com/problems/2-keys-keyboard/description/

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        #1. DP
        if n == 0:
            return n

        mem = [i+1 for i in range(n)]
        mem[0] = 0
        for i in range(1,len(mem)):
            for j in range(i-1,1,-1):
                if (i+1)%j == 0:
                    mem[i]= mem[j-1] + (i+1)//j 
                    break
        return mem[n-1]


def main():
    so = Solution()
    print so.minSteps(10)

if __name__ == '__main__':
    main()