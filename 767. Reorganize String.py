####################
#   Yaozhi Lu      #
#   Aug 13 2018    #
####################

#Origin :https://leetcode.com/problems/reorganize-string/description/

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S == '':
            return ''

        dic = {}
        for i in S:
            if dic.get(i) == None:
                dic[i] = 1
            else:
                dic[i] += 1
        res = []
        while(dic[max(dic, key=dic.get)] > 0):
            temp = max(dic, key=dic.get)
            if res != [] and temp == res[-1]:
                value = dic[temp]
                dic.pop(temp)
                if dic == {}:
                    return ''

                temp1 = max(dic, key=dic.get)
                if dic[temp1] > 0:
                    res.append(temp1)
                    dic[temp1] -= 1
                    dic[temp] = value
                else:
                    return ''

            else:
                res.append(temp)
                dic[temp] -= 1

        return ''.join(e for e in res)

def main():
    A = 'bbbbbb'
    so = Solution()
    print(so.reorganizeString(A))

if __name__ == '__main__':
    main()

