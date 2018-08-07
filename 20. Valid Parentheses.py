####################
#   Yaozhi Lu      #
#   Jul 22 2018    #
####################

#Origin: https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """ 
        l = list(s)
        open = ['(','[','{']
        close = [')',']','}']

        working = []        
        for i in l:
            if i in open:
                working.append(i)
            elif i in close:
                if working == []:
                    return False
                closed = working.pop()
                if open[close.index(i)] !=  closed:
                    return False
        
        if working == []:
            return True
        else:
            return False


def main():
    solution = Solution()
    print(solution.isValid("["))

if __name__ == "__main__":
    main()