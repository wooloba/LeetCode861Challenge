####################
#   Yaozhi Lu      #
#   Aug 14 2018    #
####################

#Origin: https://leetcode.com/problems/path-sum/description/

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        else:
            sum -= root.val
            return self.hasPathSum(root.right,sum) or self.hasPathSum(root.left,sum)

def main():
    so = Solution()
    print(so.hasPathSum(root,sum))

if __name__ == '__main__':
    main()