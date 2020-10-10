#이진 탐색 트리(BST) 합의 범위

#풀이 방법

'''
재귀구조 DFS로 브루트 포스 탐
'''

# # # # # # # # # # # # # # # # # # # # DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        return (root.val if L <= root.val <= R else 0) + \
                self.rangeSumBST(root.left, L,R) + \
                self.rangeSumBST(root.right, L,R)


# # # # # # # # # # # # # # # # # # # # 가지치기

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node: TreeNode):
            if not root:
                return 0

            if node.val <L:
                return dfs(node.right)
            elif node.val >R:
                return dfs(node.left)
            return node.val + dfs(node.left) +dfs(node.right)

        return dfs(root)

# # # # # # # # # # # # # # # # # # # # 재귀 풀이를 반복으로 변경
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root],0
        #스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L<= node.val <= R:
                    sum+=node.val
