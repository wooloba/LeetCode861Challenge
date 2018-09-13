####################
#   Yaozhi Lu      #
#   Sep 13 2018    #
####################

#Origin: https://leetcode.com/problems/student-attendance-record-i/description/


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """    
        return (list(s).count('A') <= 1) and (s.count('LLL') <= 0)

def main():
    so = Solution()
    A = 'PPALLL'

    print(so.checkRecord(A))


if __name__ == '__main__':
    main()