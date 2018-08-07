class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        x = 0
        o = 0

        win = {'OOO':0,'XXX':0}
        for i in range(3):
            if board[i] == 'OOO' or board[i] == 'XXX':
                win[board[i]] += 1
            for j in range(3):
                if board[i][j] == 'X':
                    x += 1
                elif board[i][j] == 'O':
                    o += 1
        
        for i in range(3):
            check = ''
            check += board[0][i] + board[1][i] + board[2][i]
            if check == 'OOO' or check == 'XXX':
                win[check] += 1
        
        a = board[0][0] + board[1][1] + board[2][2]
        b = board[0][2] + board[1][1] + board[2][0]

        if a == 'OOO' or a == 'XXX':
            win[a] += 1
        if b == 'OOO' or b == 'XXX':
            win[b] += 1
        

        print(o)
        print(x)
        print(win)
        if o > x or x >= o+2:
            return False
        elif win['OOO'] > 0 and win['XXX'] > 0:
            return False
        elif win['XXX'] > 0 and o >= x:
            return False
        elif win['OOO'] > 0 and x > o:
            return False
        else:
            return True 


def main():
    board = ["OOO","XX ","X  "]
    so = Solution()

    print(so.validTicTacToe(board))


if __name__ == "__main__":
    main()
