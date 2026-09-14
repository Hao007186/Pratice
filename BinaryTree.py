from collections import deque

class treenode:
    def __init__(self,val=None):
        self.val=val
        self.left=None
        self.right=None

def InsertNode(root,val):
    new_node = treenode(val)
    if root.val == None:
        root.val = new_node.val
        print('Insert successfully')

    elif new_node.val <= root.val:
        if root.left == None:
            root.left = new_node
            print('Insert successfully')
        else:
            InsertNode(root.left,val)
    else:
        if root.right == None:
            root.right = new_node
            print('Insert successfully')
        else:
            InsertNode(root.right,val)

def LevelOrder(root):
    cdeque = deque()
    if root is None:
        return None
    cdeque.append(root)
    while(len(cdeque)!=0):
        pop_node = cdeque.popleft()
        print(pop_node.val, end=' ')
        if pop_node.left != None:
            cdeque.append(pop_node.left)
        if pop_node.right != None:
            cdeque.append(pop_node.right)


def PreOrder(root):
    if root is None:
        return None
    print(root.val,end=' ')
    if root.left != None:
        PreOrder(root.left)
    if root.right != None:
        PreOrder(root.right)

def InOrder(root):
    if root is None:
        return None
    if root.left != None:
        InOrder(root.left)
    print(root.val, end=' ')
    if root.right != None:
        InOrder(root.right)

def PostOrder(root):
    if root is None:
        return None
    if root.left != None:
        PostOrder(root.left)
    if root.right != None:
        PostOrder(root.right)
    print(root.val, end = ' ')

BST= treenode()
InsertNode(BST, 40)
InsertNode(BST, 50)
InsertNode(BST, 60)
InsertNode(BST, 30)
InsertNode(BST, 20)
InsertNode(BST, 70)

PreOrder(BST)
print('')
InOrder(BST)
print('')
PostOrder(BST)
print('')
LevelOrder(BST)
