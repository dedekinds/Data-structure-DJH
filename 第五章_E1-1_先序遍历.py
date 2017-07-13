邓俊辉-数据结构-30240184_05-E1-1 先序遍历


#二叉树的先序遍历(递归版)
def preorder(tree,nodelist=None):
    if nodelist is None:
        nodelist=[]
    if tree:
        nodelist.append(tree.getRootVal())
        preorder(tree.getLeftChild(),nodelist)
        preorder(tree.getRightChild(),nodelist)
    return nodelist

#二叉树的先序遍历(递归版-简易版)
def traverse(tree):
    if tree:
        print(tree.getRootVal())
        traverse(tree.getLeftChild())
        traverse(tree.getRightChild())
