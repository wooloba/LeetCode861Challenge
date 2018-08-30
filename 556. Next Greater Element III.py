####################
#   Yaozhi Lu      #
#   Aug 29 2018    #
####################

#Origin: https://leetcode.com/problems/next-greater-element-iii/description/

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        numArray = list(str(n))
        
        wall = -1
        for i in range(len(numArray)-1,-1,-1):
            try:
                if numArray[i]<numArray[i+1]:
                    wall = i
                    break
            except:
                pass

        if wall == -1:
            return -1
        
        for i in range(len(numArray)-1,-1,-1):
                if numArray[i] > numArray[wall]:
                    temp = numArray[i]
                    numArray[i] = numArray[wall]
                    numArray[wall] = temp

                    try:
                        tempArray = numArray[wall+1:]
                        tempArray.reverse()
                        numArray[wall+1:] = tempArray
                    except:
                        pass
                    break

        if int(''.join(e for e in numArray)) > 2147483647:
            return -1
        return int(''.join(e for e in numArray))

def main():
    so = Solution()

    print so.nextGreaterElement(1999999999)


if __name__ == '__main__':
    main()

