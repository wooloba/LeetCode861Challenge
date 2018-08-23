####################
#   Yaozhi Lu      #
#   Aug 23 2018    #
####################

#Origin: https://leetcode.com/problems/trim-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        #Binary tree's left node less than root; right node greater than root
        if not root:
            return None
        
        # if root has a value less than lowest binary, then all children is less than root
        
        if root.val < L:
            return self.trimBST(root.right,L,R)

        # if root has a value greater than largest binary, then all children is greater than root
        
        elif root.val > R:
            return self.trimBST(root.left,L,R)
        
        #recursive, trim left and trim right
        root.right = self.trimBST(root.right,L,R)
        root.left = self.trimBST(root.left,L,R)
        
        return root