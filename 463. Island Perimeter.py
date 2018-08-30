####################
#   Yaozhi Lu      #
#   Aug 30 2018    #
####################

#Original:https://leetcode.com/problems/island-perimeter/description/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        primeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    primeter += self.checkBoundary([i,j],grid)


        return primeter
    
    def checkBoundary(self,location,grid):
        row = len(grid)
        col = len(grid[0])
        
        p = 0
        #UP
        if location[0] == 0 or grid[location[0]-1][location[1]] == 0:
            p += 1

        #Down
        if location[0] == row - 1 or grid[location[0]+1][location[1]] == 0:
            p += 1

        #Left
        if location[1] == 0  or grid[location[0]][location[1]-1] == 0:
            p += 1
        
        #Right
        if location[1] == col - 1 or grid[location[0]][location[1]+1] == 0:
            p += 1
        
        return p

def main():
    A = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

    so = Solution()

    print so.islandPerimeter(A)


if __name__ == '__main__':
    main()