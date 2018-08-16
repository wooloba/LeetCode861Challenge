####################
#   Yaozhi Lu      #
#   Aug 14 2018    #
####################

#Origin : https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        path = self.dfs(root)
        print(path)
        return max(e.count(',')+1 for e in path)

    def dfs(self,root):
        if root == None:
            return []

        if root.left == None and root.right == None:
            return [str(root.val)]
        
        path = [ str(root.val) +','+ e for e in self.dfs(root.left)]
        path += [ str(root.val) +','+ e for e in self.dfs(root.right)]

        return path


def main():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.right = TreeNode(5)
    tree.left.right.left = TreeNode(7)
    tree.left.left = TreeNode(6)
    
    so = Solution()
    print(so.maxDepth(tree))


if __name__ == '__main__':
    main()
        