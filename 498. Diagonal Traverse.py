####################
#   Yaozhi Lu      #
#   Aug 23 2018    #
####################

#Origin: https://leetcode.com/problems/diagonal-traverse/description/

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        diagnoal = []
        flag = 'up'

        if matrix == []:
            return matrix
        
        elif len(matrix) == 1:       
            return matrix[0]
        

        for row in range(len(matrix)):
                temp = []
                col = 0
                while row >= 0 and col < len(matrix[0]):
                    temp.append(matrix[row][col])
                    row -= 1
                    col += 1

                if flag == 'up':
                    flag = 'down'
                elif flag == 'down':
                    temp = temp[::-1]
                    flag = 'up'
                
                for e in temp:
                    diagnoal.append(e)

        #start = max(abs(len(matrix[0]) - len(matrix)) ,1)

        for col in range( 1, len(matrix[0]) ):
            print col

            temp = []
            row = len(matrix) - 1
            
            while row >= 0 and col < len(matrix[0]):
                temp.append(matrix[row][col])
                row -= 1
                col += 1

            if flag == 'up':
                flag = 'down'
            elif flag == 'down':
                temp = temp[::-1]
                flag = 'up'

            for e in temp:
                diagnoal.append(e)

        return diagnoal
            
def main():
    so = Solution()

    A = [
 [ 1, 2, 3, 4],
 [ 4, 5, 6, 8 ],
]


    print so.findDiagonalOrder(A)

if __name__ == '__main__':
    main()


    # 1  2  3  4 4.1
    # 5  6  7  8 8.1
    # 9 10 11 12 12.1



    #1 2 
    #3 4
    #5 6
    #6 7
    #8 9

    # 1 2 3 4 
    # 5 6 7 8 