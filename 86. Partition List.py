####################
#   Yaozhi Lu      #
#   Aug 30 2018    #
####################

#Origin: https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        temp = head
        smallEnd = None
        largeEnd = None
        largeStart = None

        while head != None:
            print largeEnd.val
            if head.val < x:
                if largeStart != None and smallEnd != None:
                    
                    largeEnd.next = head.next
                    head.next = largeStart
                    smallEnd.next = head
                    smallEnd = head
                    

                elif smallEnd == None:
                    smallEnd = head
                
            else:
                if largeStart == None:
                    largeStart = head
                    largeStart = head
                else:
                    largeEnd = head


            head = head.next
        return temp

def main():
    so = Solution()

    x = 3
    A = [1,3,2]
    head = ListNode(1)
    node = head

    for i in A:
        node.next = ListNode(i)
        node = node.next
    node.next = None
    #print(head.next.next.next.next.next.val)
    node = so.partition(head,x)
    

if __name__ == '__main__':
    main()
