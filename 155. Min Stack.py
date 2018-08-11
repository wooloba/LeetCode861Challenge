####################
#   Yaozhi Lu      #
#   Aug 11 2018    #
####################

#Origin: https://leetcode.com/problems/min-stack/description/

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min == None:
            self.min = x
        
        elif self.min > x:
            self.min = x

        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        item = self.stack.pop()
        if stack == []:
            self.min = None
        if item == self.min:
              self.min = min(self.stack)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


def main():
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(4)
    obj.push(-2)
    obj.push(31)
    obj.push(31)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()


if __name__ == '__main__':
    main()