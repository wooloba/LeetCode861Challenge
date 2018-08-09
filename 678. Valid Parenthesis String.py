####################
#   Yaozhi Lu      #
#   Aug 9 2018    #
####################

#Origin: https://leetcode.com/problems/valid-parenthesis-string/description/

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == '':
            return True

        open = []
        for i in s:
            print(open)
            if i == "(" or i == '*':
                open.append(i)
            elif i == ')':
                if open != [] and open[len(open)-1] == '(':
                    del open[len(open)-1]
                    
                elif open == []:
                    return False
                
                elif '(' not in open:
                    del open[len(open)-1]

                elif  open[len(open)-1] == '*' and len(open) > 0:
                    for j in range(len(open)-1,-1,-1):
                        if open[j] == '(':
                            del open[j]
                            break

        print(open)
        working = []
        for i in open:
            if i == "*":
                if working != []:
                    working.pop()
            elif i == '(':
                working.append(i)
        if working != []:
            return False

        else:
            return True


def main():
    A = "(((((()*)(*)*))())())(()())())))((**)))))(()())()"


    so = Solution()
    print(so.checkValidString(A))

if __name__ == '__main__':
    main()

