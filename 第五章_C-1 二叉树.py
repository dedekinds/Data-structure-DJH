邓俊辉-数据结构-30240184_05-C-1 二叉树

http://www.cnblogs.com/linxiyue/p/3570071.html

'''
二叉树列表实现
tree=['A',  #root
      ['B',    #左子树
       ['D',[],[]],
       ['E',[],[]]],
      ['C',     #右子树
       ['F',[],[]],
       []]
      ]
'''
def BinaryTree(item):
    return [item,[],[]]
def insertLeft(tree,item):#插入左
    leftSubtree=tree.pop(1)
    if leftSubtree:
        tree.insert(1,[item,leftSubtree,[]])
    else:
        tree.insert(1,[item,[],[]])
    return tree
def insertRight(tree,item):#插入右
    rightSubtree=tree.pop(2)
    if rightSubtree:
        tree.insert(2,[item,[],rightSubtree])
    else:
        tree.insert(2,[item,[],[]])
    return tree
def getLeftChild(tree):#获取左孩子
    return tree[1]
def getRightChild(tree):#获取右孩子
    return tree[2]


tree=BinaryTree('a')
insertLeft(tree,'b')
insertRight(tree,'c')
insertRight((getLeftChild(tree)),'d')
insertLeft((getRightChild(tree)),'e')
insertRight((getRightChild(tree)),'f')
__________________________________

'''

'''

___________________________________