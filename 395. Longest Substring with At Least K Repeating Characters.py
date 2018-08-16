####################
#   Yaozhi Lu      #
#   Aug 14 2018    #
####################

#Origin: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = []
        s = self.check(s,k)
        
        for i in s:
            if i != '':
                res += self.check(i,k)
        

        if res == []:
            return 0

        return max([len(e) for e in res])
        

    def check(self,s,k):
            dic = {}
            effective = []
            for i in s:
                try:
                    dic[i] += 1
                except:
                    dic[i] = 1
                if dic[i] >= k:
                    effective.append(i)
            
            if effective == []:
                return ''
            
            

            s = list(s)
            for i in range(len(s)):
                if s[i] not in effective:
                    s[i] = ' '
            
            s = ''.join(e for e in s)
            s = s.split(' ')

            for i in s:
                if len(i) < k:
                    s.remove(i)
            print s
            return s

        



        # s+= ' '
        # s = list(s)

        # max = 0
        # leng = 0
        # check ={}
        # for i in range(len(s)):
        #     if s[i] not in effective:
        #         print check
        #         for key in check:
        #             if check[key] < k:
        #                 leng = 0
        #         if leng > max:
        #             max = leng
        #         leng = 0
        #         check = {}
        #     else:
        #         leng += 1
        #         try:
        #             check[s[i]] += 1
        #         except:
        #             check[s[i]] = 1
        # return max


def main():
    A = "ababacb"
    k = 3

    so = Solution()

    print(so.longestSubstring(A,k))

if __name__ == '__main__':
    main()
