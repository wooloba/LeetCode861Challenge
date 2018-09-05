####################
#   Yaozhi Lu      #
#   Sep 4 2018    #
####################

#Origin: https://leetcode.com/problems/valid-sudoku/description/


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in board:
            if not self.checkList(i):
                return False
        
        for i in range(9):
            nums = []
            for j in range(9):
                if board[j][i] != '.':
                    nums.append(board[j][i])
            if not self.checkList(nums):
                return False
        

        numList = [[]for e in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    numList[j/3].append(board[i][j])
            
            if i == 2 or i == 5 or i == 8:
                print numList
                for k in numList:
                    if not self.checkList(k):
                        return False
                numList = [[]for e in range(3)]

        return True
    

    def checkList(self, nums):
        dic = {}
        for i in nums:
            if i != '.':
                if not dic.get(i):
                    dic[i] = 1
                else:
                    return False
        return True


def main():
    so = Solution()

    A = [  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]]

    print so.isValidSudoku(A)

if __name__ == '__main__':
    main()

