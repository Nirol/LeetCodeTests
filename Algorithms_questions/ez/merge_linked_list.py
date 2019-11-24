# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x = None):
    self.val = x
    self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        l1_string=""
        l2_string = ""
        while l1:
            l1_string+=str(l1.val)
            l1=l1.next
        while l2:
            l2_string+=str(l2.val)
            l2=l2.next
        l1_num = int(l1_string[::-1])
        l2_num = int(l2_string[::-1])
        sum = str(l1_num+l2_num)
        list_result=ListNode(sum[0])
        list_result_head=list_result
        for char in sum[1:]:
            list_result.next=ListNode(char)
            list_result=list_result.next

        return list_result_head
  #
  #
  # def skip_middle_node(self, l1):
  #     if l1 is None:
  #         return
  #     while l1.next is not None:
  #         l1.val=l1.next.val
  #         if l1.next.next is None:
  #             l1.next = None
  #             return
  #         l1=l1.next
  #
  # def partiton_list(self, l1, value):
  #       before_value = None
  #       after_value = None
  #       value_list = None
  #       while l1 is not None:
  #           next = l1.next
  #           if l1.val < value:
  #               l1.next = before_value
  #               before_value=l1
  #
  #           elif l1.val >= value:
  #               l1.next = after_value
  #               after_value=l1
  #
  #           l1=next
  #
  #       if before_value is None:
  #           return after_value
  #
  #       head = before_value
  #       while before_value.next is not None:
  #           before_value = before_value.next
  #       before_value.next = after_value
  #
  #       return head



if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)



    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    while result:
      print (result.val)
      result = result.next

