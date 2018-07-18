####################
#   Yaozhi Lu      #
#   Jul 18 2018    #
####################

#Origin: https://leetcode-cn.com/problems/isomorphic-strings/description/


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        A = list(s)
        B = list(t)

        if len(A)!= len(B):
            return False
        
        if self.checkIsomorphic(A,B) and self.checkIsomorphic(B,A):
            return True
        else:
            return False
    
    def checkIsomorphic(self,A,B):
        dic= {}
        for i in range(0,len(A)):
            if A[i] in dic:
                value = dic[A[i]]
                if value != B[i]:
                    return False
                else:
                    continue
            else:
                dic[A[i]] = B[i]
        
        return True



def main():
    solution = Solution()
    print solution.isIsomorphic("title","paper")


if __name__ == "__main__":
    main()