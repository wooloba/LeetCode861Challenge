####################
#   Yaozhi Lu      #
#   Aug 8 2018    #
####################

#Origin: https://leetcode.com/problems/ransom-note/description/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        m = len(matrix)
        n = len(matrix[0])

        replace = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    replace.append([i,j])
        
        for zero in replace:
            matrix[zero[0]] = [0] * n
            for i in range(m):
                matrix[i][zero[1]] = 0
            

        return matrix

def main():
    A = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    so = Solution()
    print(so.setZeroes(A))

if __name__ == '__main__':
    main()