num = int(input())
tree = {}

class binaryTree:
    def __init__(self,root,left,right):
        self.rootNode = root
        self.leftNode = left
        self.rightNode = right


for _ in range(num):
    root, lef, rig = map(str,input().split())
    tree[root] = binaryTree(root,lef,rig)

def preorder(node):
    print(node.rootNode, end= '')
    if node.leftNode!='.':
        preorder(tree[node.leftNode])
    if node.rightNode!='.':
        preorder(tree[node.rightNode])

def inorder(node):
    if node.leftNode!='.':
        inorder(tree[node.leftNode])
    print(node.rootNode, end='')
    if node.rightNode!='.':
        inorder(tree[node.rightNode])

def postorder(node):
    if node.leftNode!='.':
        postorder(tree[node.leftNode])
    if node.rightNode!='.':
        postorder(tree[node.rightNode])
    print(node.rootNode, end='')

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])