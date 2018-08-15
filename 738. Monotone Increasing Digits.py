####################
#   Yaozhi Lu      #
#   Aug 14 2018    #
####################

#Origin : https://leetcode.com/problems/monotone-increasing-digits/description/

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 10:
            return N

        wall = None
        Nlist = [int(e) for e in str(N)]
        i = len(Nlist)-1
        while i > 0:
            if Nlist[i] < Nlist[i-1]:
                Nlist[i-1] -= 1
                wall = i
            i -= 1
        if wall != None:
            for i in range(wall,len(Nlist)):
                Nlist[i] = 9

        return int(''.join(str(e) for e in Nlist))

    # def check(self,N):
    #     Nlist = [int(e) for e in str(N)]
    #     for i in range( len(Nlist)-1 ):
    #         if Nlist[i] > Nlist[i+1]:
    #             return False
    #     return True


def main():
    so = Solution()
    print(so.monotoneIncreasingDigits(1234))

if __name__ == "__main__":
    main()