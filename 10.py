#You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        str1 = ''.join(str(e) for e in l1)[::-1]
        str2 = ''.join(str(e) for e in l2)[::-1]
        i1 = int(str1)
        i2 = int(str2)
        i3 = i1 + i2
        str3 = str(i3)
        l3 = []
        for i in reversed(str3):
            l3.append(int(i))
        return l3


sol = Solution()

l1 = [2,4,9]
l2 = [5,6,4,9]

x = sol.addTwoNumbers(l1, l2)

print(x)

