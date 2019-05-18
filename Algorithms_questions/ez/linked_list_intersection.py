# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ll_a_length = Solution.get_link_list_length(self,headA)
        ll_b_length = Solution.get_link_list_length(self,headB)
        diff_length = abs(ll_a_length-ll_b_length)
        temp_short=[]
        temp_long=[]

        if ll_a_length <= ll_b_length:
            temp_short = headA
            temp_long = headB
        else:
            temp_short = headB
            temp_long = headA

        for i in range(diff_length):
            temp_long = temp_long.next

        while  temp_long is not None:
            if temp_long == temp_short:
                return temp_long
            else:
                temp_long = temp_long.next
                temp_short = temp_short.next

        return None


    def get_link_list_length(self,ll):
        """
        :type ll: ListNode
        :rtype: int
        """
        ll_length = 0
        temp_list = ll
        while temp_list is not None:
            ll_length = ll_length + 1
            temp_list = temp_list.next
        return ll_length