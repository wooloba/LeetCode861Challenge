class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i] = A[i][::-1]
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    A[i][j] = 0
                else:
                    A[i][j] = 1

        
        return A


def main():
    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    solution = Solution()
    print(solution.flipAndInvertImage(A))



if __name__ == '__main__':
    main()