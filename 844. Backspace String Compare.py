####################
#   Yaozhi Lu      #
#   Aug 11 2018    #
####################

#Origin:https://leetcode.com/problems/backspace-string-compare/description/

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        print(self.gen(S))
        return self.gen(S) == self.gen(T)



    def gen(self,S):
        S = list(S)
        i = 0
        while i < len(S):
            if S[i] == '#':
                del S[i]
                if i > 0:
                    del S[i-1]
                    i -= 1
                continue
            else:
                i += 1
        return ''.join( e for e in S)


def main():
    S = "ab##"
    T = "a#d#"
    so = Solution()
    print(so.backspaceCompare(S,T))

if __name__ == '__main__':
    main()
