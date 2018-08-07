####################
#   Yaozhi Lu      #
#   Jul 20 2018    #
####################

#Origin: https://leetcode.com/problems/reordered-power-of-2/description/

class Solution:
    # def checkPowerOf2(self,N):
    #     return N != 0 and ((N & (N - 1)) == 0)

    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        l = sorted(list(str(N)))
        k = [sorted(str(2**e)) for e in range(0,30)]
        if l in k:
            return True
        else:
            return False

            
        # for i in range(len(l)):
        #     l.append(l.pop(0))
        #     print(l)
        #     if l[0] != '0':
        #         k = ''.join(e for e in l)
        #         print(k)
        #         if self.checkPowerOf2(int(k)):
        #             return True
        #         else:
        #             pass


def main():
    solution = Solution()
    print(solution.reorderedPowerOf2(218))

if __name__ == "__main__":
    main()