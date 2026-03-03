#        TREES
#code to demonstrate traversal in a binary search tree
print("1.inorder")
values=list(map(int,input("enter values in a BST pattern:").split()))
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,value):
        if root is None:
            return node(value)
        if value<root.data:
            root.left=insert(root.left,value)
        else:
            root.right=insert(root.right,value)
        return root
def inorder(root):
    if root:
        #print(root.data,end=" ")#pre order
        inorder(root.left)
        #print(root.data,end=" ")#in order
        inorder(root.right)
        print(root.data,end=" ")#post order


root=None
for v in values:
    root=insert(root,v)
print("post order traversal:",inorder(root))    


'''print("2.preorder")
values=list(map(int,input("enter values in a BST pattern:").split()))
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,value):
        if root is None:
            return node(value)
        if value<root.data:
            root.left=insert(root.left,value)
        else:
            root.right=insert(root.right,value)
        return root
def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

root=None
for v in values:
    root=preorder(root,v)
print("perorder traversal:",preorder(root))   
'''
