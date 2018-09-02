####################
#   Yaozhi Lu      #
#   Sep 1 2018    #
####################

#Origin:https://leetcode.com/problems/longest-common-prefix/description/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        prefix = strs[0]

        for i in range(1,len(strs)):
            if strs[i] == '' or prefix == '' or prefix[0] != strs[i][0] :
                return ''
            for j in range(0,min(len(strs[i]),len(prefix))):

                if prefix[j] != strs[i][j]:
                    prefix = prefix[0:j]
                    break
                
                if  prefix == '':
                    return prefix
                
            if prefix != strs[i]:
                if len(prefix) > len(strs[i]):
                    prefix = strs[i]
                else:
                    pass
        return prefix


def main():
    so = Solution()
    A = ['','']
    print so.longestCommonPrefix(A)

if __name__ == '__main__':
    main()

