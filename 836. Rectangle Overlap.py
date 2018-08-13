####################
#   Yaozhi Lu      #
#   Aug 13 2018    #
####################

#Origin:https://leetcode.com/problems/rectangle-overlap/description/

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return (rec1[0]<rec2[2] and rec1[2] > rec2[0]) and (rec1[1] < rec2[3] and rec1[3]>rec2[1])


def main():
    rec1 = [1,1,2,2]
    rec2 = [0,0,3,3]
    so =Solution()
    print(so.isRectangleOverlap(rec1,rec2))

if __name__ == '__main__':
    main()