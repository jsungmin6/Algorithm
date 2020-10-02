#두 정렬 리스트의 병합

'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

#풀이 방법
#연결 리스트 이해 안감.
'''
1.두 정렬 리스트를 비교해 작은게 왼쪽에 가게하는 재귀함수 생성
'''

# # # # # # # # # # # # # # # # # # # # #
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, 12 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next,l2)
        return l1
        
