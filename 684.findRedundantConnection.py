####################
#   Yaozhi Lu      #
#   Jul 18 2018    #
####################

#Origin: https://leetcode-cn.com/problems/redundant-connection/description/


class Solution(object):
    def findRedundantConnection(self, edges):
        nodes = list(set(sum(edges,[])))
        nodes = dict.fromkeys(nodes, 0)
        
        


def main():
    solution = Solution()
    print solution.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])


if __name__ == "__main__":
    main()