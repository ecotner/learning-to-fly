"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Solution:
- Go through each linked list, turn it into a string, then reverse the string and convert to integer. Add the two
together, then convert back into a linked list.
- Go through two linked lists simultaneously. Add nodes together directly, and if the result is > 10, just add 1 to
the next node.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        value = l1.val + l2.val
        if value < 10:
            lr = ListNode(value)
            carry = 0
        else:
            lr = ListNode(value % 10)
            carry = 1
        l3 = lr
        while (l1.next is not None) and (l2.next is not None):
            l1 = l1.next
            l2 = l2.next
            value = l1.val + l2.val + carry
            if value < 10:
                l3.next = ListNode(value)
                carry = 0
            else:
                l3.next = ListNode(value % 10)
                carry = 1
            l3 = l3.next
        if (l1.next is None):
            while (l2.next is not None):
                l2 = l2.next
                value = l2.val + carry
                if value < 10:
                    l3.next = ListNode(value)
                    carry = 0
                else:
                    l3.next = ListNode(value % 10)
                    carry = 1
                l3 = l3.next
        elif (l2.next is None):
            while (l1.next is not None):
                l1 = l1.next
                value = l1.val + carry
                if value < 10:
                    l3.next = ListNode(value)
                    carry = 0
                else:
                    l3.next = ListNode(value % 10)
                    carry = 1
                l3 = l3.next
        if (l1.next is None) and (l2.next is None):
            if carry == 1:
                l3.next = ListNode(carry)
            return lr
