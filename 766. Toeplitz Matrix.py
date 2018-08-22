####################
#   Yaozhi Lu      #
#   Aug 21 2018    #
####################

#Origin: https://leetcode.com/problems/toeplitz-matrix/description/

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            temp = i
            j = 0 
            
            while j < n and i < m:
                if matrix[i][j] != matrix[temp][0]:
                    return False
                j += 1
                i += 1
            i = temp
        
        for i in range(1,n):
            temp = i
            j= 0

            while j < m and i <n:
                if matrix[j][i] != matrix[0][temp]:
                    return False
                i+=1
                j+=1
            i = temp

        return True


def main():
    A = [[11,74,0,93],[40,11,74,7]]
    so = Solution()
    print(so.isToeplitzMatrix(A))


if __name__ == '__main__':
    main()
