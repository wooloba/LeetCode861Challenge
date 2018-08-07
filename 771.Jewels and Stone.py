####################
#   Yaozhi Lu      #
#   Jul 22 2018    #
####################

#Origin: https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        J = list(J)
        for i in S:
            if i in J:
                count += 1
        return count


def main():
    solution = Solution()
    print(solution.numJewelsInStones('aA','aAAbbbb'))

if __name__ == "__main__":
    main()
