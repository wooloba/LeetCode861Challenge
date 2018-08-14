####################
#   Yaozhi Lu      #
#   Aug 14 2018    #
####################

#Origin: https://leetcode.com/problems/lemonade-change/description/

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        cash = []

        for i in bills:
            if i == 5:
                cash.append(i)
            elif i == 10:
                try:
                    del cash[cash.index(5)]
                except:
                    return False
                cash.append(10)
            elif i == 20:
                try:
                    del cash[cash.index(10)]
                    del cash[cash.index(5)]
                except:
                    try:
                        for i in range(3):
                            del cash[cash.index(5)]
                    except:
                        return False
        return True

def main():
    A = [5,5,10,10,20]
    so = Solution()
    print(so.lemonadeChange(A))

if __name__ == '__main__':
    main()                
