####################
#   Yaozhi Lu      #
#   Aug 9 2018    #
####################

# Origin: https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        while n > 0:
            n /=5
            k += n

        return k

def main():
    so = Solution()
    print(so.trailingZeroes(7027))

if __name__ == '__main__':
    main()


# i = list(str(self.factorial(n)))
#         k = 0
#         for j in range(len(i)-1 , -1 , -1):
#             if i[j] == '0':
#                 k += 1
#             else:
#                 break

#         return k
    
#     def factorial(self,n):
#         if n < 1 :
#             return 1
#         else:
#             return n * self.factorial(n-1)