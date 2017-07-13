邓俊辉-数据结构-30240184_05-E1-1 先序遍历

____________________________________
#二叉树的先序遍历(递归版)
def preorder(tree,nodelist=None):
    if nodelist is None:
        nodelist=[]
    if tree:
        nodelist.append(tree.getRootVal())
        preorder(tree.getLeftChild(),nodelist)
        preorder(tree.getRightChild(),nodelist)
    return nodelist
____________________________________
#二叉树的先序遍历(递归版-简易版)
def traverse(tree):
    if tree:
        print(tree.getRootVal())
        traverse(tree.getLeftChild())
        traverse(tree.getRightChild())
____________________________________
#二叉树的先序遍历（迭代版）
#需要用到栈
def preorder(tree):
    s=Stack()
    if tree:
        s.push(tree)#根节点入栈（初始化,但不是值入栈
    while s.isEmpty()!=True:
        temp=s.pop()
        print(temp.getRootVal())
        if temp.getRightChild():
            s.push(temp.getRightChild())
        if temp.getLeftChild():
            s.push(temp.getLeftChild())
_____________________________________  
#二叉树的先序遍历（迭代可扩展版）
#需要用到栈
def visitAlongLeftBranch(tree,s):#不断地遍历左边，将右孩子推入栈中
    while tree:
        print(tree.getRootVal())
        s.push(tree.getRightChild())
        tree=tree.getLeftChild()

def travPre(tree):
    s=Stack()
    while True:
        visitAlongLeftBranch(tree,s)
        if s.isEmpty():
            break
        tree=s.pop()
