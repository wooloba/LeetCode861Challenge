####################
#   Yaozhi Lu      #
#   Aug 22 2018    #
####################


#Origin: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        dic = {}
        temp = head

        while head != None:
            
            if dic.get(head.val) == None:
                dic[head.val] = 1
            else:
                dic[head.val] += 1
            head = head.next

        print(dic)

        head = temp
        temp = temp.next

        while dic[head.val] != 1 and temp != None:
            head = temp
            temp = temp.next

        if dic[head.val] != 1:
            return None
        
        temp1 = head

        while temp != None:
            if  dic[temp.val] != 1:
                while temp != None and dic[temp.val] != 1:
                    temp = temp.next
                temp1.next = temp

            try:
                temp = temp.next
                temp1 = temp1.next
            except:
                pass

        return head

    def PList(self, head):
        node = self.deleteDuplicates(head)

        while node.next != None:
            print(node.val)


def main():
    
    a = [1,2,2]
    
    head = ListNode(a[0])
    head.next = ListNode(a[1])
    head.next.next = ListNode(a[1])
    
    so = Solution()

    so.PList(head)

if __name__ == '__main__':
    main()

