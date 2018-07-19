
####################
#   Yaozhi Lu      #
#   Jul 19 2018    #
####################
#Origin: https://leetcode.com/problems/add-two-numbers/description/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = []
        link = l1
        while (link!=None):
            num1.insert(0,str(link.val))
            link = link.next
        num1 = int(''.join(e for e in num1))

        num2 = []
        node = l2
        while (node!=None):
            num2.insert(0,str(node.val))
            node = node.next
        num2 = int(''.join(e for e in num2))

        result = list(str(num1+num2))[::-1]

        l3 = ListNode(result[0])
        temp = l3
        for i in range(1,len(result)):
            node = ListNode(result[i])
            temp.next = node
            temp = node

        temp.next = None

        return l3


def main():
    solution = Solution()
    #  ...
    l1 = ListNode(2)
    temp = ListNode(4)
    temp2 = ListNode(3)

    l1.next = temp
    temp.next = temp2
    temp2.next = None

    l2 = ListNode(5)
    temp = ListNode(6)
    temp2 = ListNode(5)

    l2.next = temp
    temp.next = temp2
    temp2.next = None


    l3 = solution.addTwoNumbers(l1,l2)
    
    while (l3!= None):
        print(l3.val)
        l3 = l3.next

    #print solution.addTwoNumbers([3,2,4],6)


if __name__ == "__main__":
    main()