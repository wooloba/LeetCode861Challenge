####################
#   Yaozhi Lu      #
#   Aug 23 2018    #
####################

#Origin: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        if not root:
            return 0
        if not root.children:
            return 1
        else:
            return max(self.maxDepth(node) for node in root.children) + 1

def main():
    so = Solution()
    
    print(so.maxDepth(root))


if __name__ == '__main__':
    main()

