####################
#   Yaozhi Lu      #
#   Sep 4 2018    #
####################

#Origin: https://leetcode.com/problems/projection-area-of-3d-shapes/description/

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        for i in range(len(grid)):
            area += max(grid[i])
            maxCol = 0
            for j in range(len(grid[i])):
                if grid[j][i] > 0:
                    area += 1
                    if grid[j][i] > maxCol:
                        maxCol = grid[j][i]
            area += maxCol
            maxCol = 0


        return area

def main():
    so =Solution()
    A = [[1,0],[0,2]]
    print so.projectionArea(A)

if __name__ == '__main__':
    main()


                    
