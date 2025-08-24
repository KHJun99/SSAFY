# 백준_1991_트리 순회 (s1)
"""
문제
이진 트리를 입력받아 전위 순회, 중위 순회, 후위 순회 한 결과를 출력하는 프로그램을 작성하시오.

기본 개념
1. 전위 순회 : VLR
2. 중위 순회 : LVR
3. 후위 순회 : LRV
"""
class node():
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def preorder(now, out):
    out.append(tree[now].key)
    if tree[now].left != '.':
        preorder(tree[now].left, out)
    if tree[now].right != '.':
        preorder(tree[now].right, out)

def inorder(now, out):
    if tree[now].left != '.':
        inorder(tree[now].left, out)
    out.append(tree[now].key)
    if tree[now].right != '.':
        inorder(tree[now].right, out)

def postorder(now, out):
    if tree[now].left != '.':
        postorder(tree[now].left, out)
    if tree[now].right != '.':
        postorder(tree[now].right, out)
    out.append(tree[now].key)


N = int(input())
tree = {}
for _ in range(N):
    n, l, r = map(str, input().split())
    tree[n] = node(n, l, r)

pre, ino, post = [], [], []
preorder('A', pre)
inorder('A', ino)
postorder('A', post)

print(*pre, sep = '')
print(*ino, sep = '')
print(*post, sep = '')



