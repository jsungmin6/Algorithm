#역순 연결 리스트

'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

#풀이 방법
#재귀호출 구조 이해는 가는데 이걸 내가 짤 수 있나..?
#이 구조는 외우는게 나을 것 같음.
'''
1.두 정렬 리스트를 비교해 작은게 왼쪽에 가게하는 재귀함수 생성
'''

# # # # # # # # # # # # # # # # # # # # #
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 재귀구조
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def revese(node:ListNode, prev:ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next,node)
        return reverse(head)
'''
스택을 그려보면
reverse(None,5 4 3 2 1 None)
- - - - - - - - - - - -
reverse(5, 4 3 2 1 None)
- - - - - - - - - - - -
reverse(4 5,3 2 1 None)
- - - - - - - - - - - -
reverse(3 4 5, 2 1 None)
- - - - - - - - - - - -
reverse(2 3 4 5, 1 None)
'''
#반복구조
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
