####################
#   Yaozhi Lu      #
#   Aug 8 2018    #
####################
#Origin: https://leetcode.com/problems/rotate-string/description/

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A==B:
            return True
        for i in range(len(A)):
            A = list(A)
            A.append(list(A)[0])
            del A[0]
            A = ''.join(e for e in A)
            if A == B:
                return True
        
        return False

def main():
    A = ''
    B = ''
    so = Solution()
    print(so.rotateString(A,B))


if __name__ == '__main__':
    main()