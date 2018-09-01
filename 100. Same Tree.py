####################
#   Yaozhi Lu      #
#   Aug 31 2018    #
####################

#Origin:https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
        return False
        
