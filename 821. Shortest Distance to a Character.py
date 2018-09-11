####################
#   Yaozhi Lu      #
#   Sep 10 2018    #
####################

#Origin:https://leetcode.com/problems/shortest-distance-to-a-character/description/

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        result = [10001 for i in S]
        
        S = list(S)
        leng = 0
        for i,e in enumerate(S):
            if e == C:
                result[i] = 0
                for j in range(i-leng,i):
                    result[j] = leng
                    leng -= 1
            else:
                leng += 1
        print result    

        result = result[::-1]
        leng = 0
        for i,e in enumerate(S[::-1]):
            if e == C:
                k = 1
                for j in range(i-1,i-leng-1,-1):
                    if k < result[j]:
                        result[j] = k
                    k += 1
            else:
                leng += 1

        return result[::-1]


def main():
    so = Solution()
    A = 'loveleetcode'
    C = 'l'
    
    print so.shortestToChar(A,C)

if __name__ == '__main__':
    main()