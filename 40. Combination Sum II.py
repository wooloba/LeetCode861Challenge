####################
#   Yaozhi Lu      #
#   Aug 24 2018    #
####################

#Origin https://leetcode.com/problems/combination-sum-ii/description/

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        

        dyli = [set() for i in range(target+1)]
        dyli[0].add(())

        candidates.sort()

        for i in candidates:
            print dyli
            if i > target:
                break
            for remain in range(target,i-1,-1):
                for j in dyli[remain-i]:
                    dyli[remain].add(j+(i,))
        
        return [list(e) for e in dyli[-1]]

def main():
    so = Solution()

    A = [10,1,2,7,6,1,5]
    target = 8

    print so.combinationSum2(A,target)


if __name__ == '__main__':
    main()            