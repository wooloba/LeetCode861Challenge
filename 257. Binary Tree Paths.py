####################
#   Yaozhi Lu      #
#   Aug 14 2018    #
####################

# Origin: https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        if root.right == None and root.left == None:
            return [str(root.val)]

        path = [str(root.val) + '->' + e for e in self.binaryTreePaths(root.left)]
        path += [str(root.val) + '->' + e for e in self.binaryTreePaths(root.right)]
        return path

    #     result = []
    #     ori = root
    #     self.findPath(result,root,ori)
    #     print(result)
    # def findPath(self,result,root,ori):
    #     while root != None:
    #         result.append(str(root.val))
    #         print('left:'+str(ori.val))
    #         if root.right == None and root.left == None:
    #             root = ori
    #             result.append('*')
    #             return
    #             #self.findPath(result,ori,ori)
    #         else:
    #             return self.findPath(result,root.left,ori) or self.findPath(result,root.right,ori)


def main():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.right = TreeNode(5)
    tree.left.right.left = TreeNode(7)
    tree.left.left = TreeNode(6)
    
    so = Solution()
    print(so.binaryTreePaths(tree))


if __name__ == '__main__':
    main()
