'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.
'''
#题目要求：单链表，要求删除任一非尾部节点，并且只给定当前节点
#解题思路：由于只给了当前节点，无法用到上一节点来操作，所以，将当前节点的下个节点的值赋值给当前节点，然后将当前节点的链接区指向下个节点的链接区（指向None），相当于删掉了最后一个节点。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
