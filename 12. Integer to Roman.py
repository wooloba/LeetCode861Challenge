####################
#   Yaozhi Lu      #
#   Jul 17 2018    #
####################

#Origin: https://leetcode.com/problems/integer-to-roman/description/
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        sym = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        spe = {4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}
        n = [1,5,10,50,100,500,1000]
        roman = ''

        num = list(str(num))

        for i in range(len(num)):
            if int(num[i]) == 0:
                continue

            index = int(num[i]) * 10**(len(num)-i-1)
            if int(num[i]) in [4,9]:
                roman += spe[int(num[i]) * 10**(len(num)-i-1)]
                continue

            i = len(n)-1
            while index != 0:
                print(i)
                if index - n[i] >= 0:
                    roman += sym[n[i]]
                    index -= n[i]
                    
                if i >0 and index < n[i]:
                    i -= 1
        
        return roman

def main():
    so = Solution()
    print(so.intToRoman(20))


if __name__ == '__main__':
    main()

