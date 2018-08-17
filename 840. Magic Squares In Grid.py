####################
#   Yaozhi Lu      #
#   Aug 16 2018    #
####################

# Origin: https://leetcode.com/problems/magic-squares-in-grid/description/

class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        count = 0

        for i in self.findAll(grid):
            if self.check(i):
                count += 1
        return count


    def findAll(self,grid):
        grids = []
        for i in range(0, len(grid)-2):
            for j in range(0, len(grid[0])-2):
                grids.append([[grid[i][j], grid[i][j+1], grid[i][j+2]],
                                [grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2]],
                                [grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]
                                ])
        
        print(grids)
        return grids

    
    def check(self,g):   
        su = sum(g[0])
        for i in g:
            if sum(i) != su :
                return False
        for i in range(0,2):
            if g[0][i]+g[1][i]+g[2][i] != su:
                return False

        if g[0][0] + g[1][1] +g[2][2] != su or g[0][2]+g[1][1]+g[2][0] != su:
            return False
        
        for i in g:
            for j in i:
                if j>9 or j<1:
                    return False
        return True


def main():
    A = [[10,3,5],[1,6,11],[7,9,2]]

    so = Solution()

    print(so.numMagicSquaresInside(A))

if __name__ == '__main__':
    main()