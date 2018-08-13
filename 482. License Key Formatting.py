####################
#   Yaozhi Lu      #
#   Aug 13 2018    #
####################

#Origin: https://leetcode.com/problems/license-key-formatting/description/

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        li = ''.join(e for e in S.split('-')).upper()
        res = []
        if len(li)%K != 0:
            res.append(li[0:len(li)%K])
        
        for i in range(len(li)%K,len(li),K):
            res.append(li[i:i+K])

        return '-'.join(e for e in res)


def main():
    A = '2-5g-3-j'
    k = 2
    so = Solution()
    print(so.licenseKeyFormatting(A,k))

if __name__ == '__main__':
    main()