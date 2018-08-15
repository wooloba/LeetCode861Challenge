####################
#   Yaozhi Lu      #
#   Aug 14 2018    #
####################

#Origin :https://leetcode.com/problems/hamming-distance/description/

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        A = bin(x)[2:].zfill(32)
        B = bin(y)[2:].zfill(32)

        diff = 0
        for i in range(32):
            if A[i] != B[i]:
                diff += 1
        
        return diff

def main():
    so =Solution()
    print(so.hammingDistance(42342,4234234))


if __name__ == '__main__':
    main()