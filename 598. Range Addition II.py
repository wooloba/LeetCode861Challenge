####################
#   Yaozhi Lu      #
#   Aug 20 2018    #
####################

#Origin:https://leetcode.com/problems/range-addition-ii/description/

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        minx = 40000
        miny = 40000
        if ops = []:
            return m*n
        for i in ops:
            if i[0]< minx:
                minx = i[0]

            if i[1] < miny:
                miny = i[1]

        return minx*miny 


        # array  = [[0]*n for i in range(m)]
        
        # for i in ops:
        #     for j in range(i[1]):
        #         for k in range(i[0]):
        #             array[j][k] += 1

        # num = 0
        # for i in array:
        #     num += i.count(array[0][0])
        
        # return num

def main():
    so = Solution()
    A = [[1,2],[3,3]]
    print(so.maxCount(3,3,A))

if __name__ == '__main__':
    main()