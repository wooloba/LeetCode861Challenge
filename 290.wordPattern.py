####################
#   Yaozhi Lu      #
#   Jul 17 2018    #
####################

#Origin: https://leetcode-cn.com/problems/word-pattern/description/

class leetCodeSolution():
    def wordPattern(self, pattern, str):
        dic = {}
        pattern = list(pattern)
        string = str.split(' ')

        if len(pattern)!=len(string):
            return False
        for i in range(0,len(pattern)):
            try:
                value = dic[pattern[i]]
                if value != string[i]:
                    return False
                else:
                    continue
            except:
                if string[i] not in dic.values():
                    dic[pattern[i]] = string[i]
                else:
                    return False
            print(dic)
        return True



def main():
    solution = leetCodeSolution()
    print solution.wordPattern("abba","dog dog dog dog")


if __name__ == "__main__":
    main()