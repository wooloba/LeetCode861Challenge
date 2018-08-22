####################
#   Yaozhi Lu      #
#   Aug 22 2018    #
####################

#Origin: https://leetcode.com/problems/add-strings/description/

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        return self.numConvertor(num1) + self.numConvertor(num2)

    def numConvertor(self,num):
        dic = {'1': 1, '3': 3, '2': 2, '5': 5, '4': 4, '7': 7, '6': 6, '9': 9, '8': 8}

        a = 0
        for i in range(len(num)):
            a += dic[num[i]] * (10 ** (len(num)-i-1))
        return a

def main():
    so = Solution()
    print so.addStrings('123','237')

if __name__ == '__main__':
    main()