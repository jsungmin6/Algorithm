N=int(input())
graph={}
for _ in range(N):
    node,left,right = input().split()
    graph[node] = [left,right]

root='A'
preorders=[]
inorders=[]
postorders=[]
def preorder(n):
    left,right = graph[n][0],graph[n][1]
    preorders.append(n)
    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)


def inorder(n):
    left,right = graph[n][0],graph[n][1]
    if left != '.':
        inorder(left)
    inorders.append(n)
    if right != '.':
        inorder(right)

def postorder(n):
    left,right = graph[n][0],graph[n][1]
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    postorders.append(n)

preorder(root)
inorder(root)
postorder(root)
print(''.join(preorders))
print(''.join(inorders))
print(''.join(postorders))