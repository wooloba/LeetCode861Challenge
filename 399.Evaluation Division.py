####################
#   Yaozhi Lu      #
#   Jul 22 2018    #
####################

# Origin: https://leetcode.com/problems/evaluate-division/description/


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        charValue = {}

        charValue[equations[0][0]] = 1

        i = 0
        while i < len(equations):
            for k in [0,1]:
                if len(equations[i][k]) > 1:
                    A = list(equations[i][k])
                    Aval = 1.0
                    for j in A:
                        try:
                            Aval *= charValue[i]
                        except:
                            break
                    charValue[A] = Aval
                    equations[i] = []

            if charValue.get(equations[i][0]) != None:
                charValue[equations[i][1]] = float(charValue.get(equations[i][0])) / values[i]
                equations.remove(equations[i])
                del values[i]
            elif charValue.get(equations[i][1]) != None:
                charValue[equations[i][0]] = float(charValue.get(equations[i][0])) * values[i]
                equations.remove(equations[i])
                del values[i]
            else:
                i+=1
        
        result = []
        for i in queries:
            try:
                answer = charValue[i[0]] / charValue[i[1]]
                result.append(float(answer))
            except:
                result.append(-1.0)
        
        return result


def main():
    solution = Solution()
    k = solution.calcEquation([ ["a", "b"], ["b", "c"] ],[2.0, 3.0],[ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
    print(k)
if __name__ == '__main__':
    main()
