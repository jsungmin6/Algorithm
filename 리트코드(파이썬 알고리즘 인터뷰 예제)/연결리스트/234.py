#팰린드롬 연결 리스트

'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
'''

#풀이 방법

'''
1.연결리스트 자료형으로 데이터가 input(처음 봄)
2.연결리스트 자료형을 리스트 자료형으로 바꿔서 해결
3.그대로 연결리스트 자료형으로 해결
'''

# # # # # # # # # # # # # # # # # # # # #
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         q:Deque = collections.deque()
#
#         if not head:
#             return True;
#
#         node=head
#         while node is not None:
#             q.append(node.val)
#             node = node.next
#
#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False;
#
#         return True

###########################################

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        #런너를 이용해 역순 연결 리스트 구성

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        #만약 1 2 3 2 1 면 현재 slow는 2->1 이고 rev 는 2->1->None 인 상황임. 홀수일 때 slow가 3->2 이렇게 가운대에서 멈추기에 fast가 남아있으면 한칸 더 next처리 해 준 것
        #이 코드 부분은 외우는게 좋을 듯.

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
